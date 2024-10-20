import sys
import numpy as np
from numpy import pi, cos, sin, exp, log
from numpy.linalg import norm
import scipy as sp
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functools import partial
from pathos.multiprocessing import ProcessingPool as Pool

type triplet = tuple[float, float, float]


# A progress bar intended for large 'for loop' calculations
def progress_bar(i, N, buffer) -> None:
    if i % buffer == 0 or i == N-1:
        sys.stdout.write('\r')
        j = (i + 1)/N
        sys.stdout.write("[%-20s] %d%%" % ('='*int(20*j), 100*j))
        sys.stdout.flush()


def serial_computation(function: callable, number_of_calculations: int, *args, **kwargs) -> list[any]:
    output = []
    for i in range(number_of_calculations):
        output.append(function(*args, **kwargs))

    return output


def parallel_computation(function: callable, number_of_calculations, number_of_cores: int, *args, **kwargs) -> list[any]:
    with Pool(number_of_cores) as pool:
        output = pool.map(function, *args, **kwargs)

    return output


class Thread:
    def __init__(self) -> None:
        """
        Object has four main attributes organized as follows:
        - self.lattice_data = (lattice_constants, super_cell, size, positions, number_of_spins)
        - self.bond_data = (bond_dic, adjacency_tensor, exchange_matrices)
        - self.time_evolution_data = (dt, tf, time_evolution)
        - self.DSF_data = (steps, path, DSF)
        """

        lattice_data = ['lattice_constants', 'super_cell', 'size', 'positions', 'number_of_spins']
        magnetic_structure = ["exchange_matrices", "adjacency_matrices",
                              "adjacency_exchange_tensor", "color", "external_field"]
        time_evolution_data = ['dt', 'tf', 'time_evolution']
        dsf_data = ['steps', 'path', 'DSF']

        self.lattice: dict[str, any] = dict.fromkeys(lattice_data)
        self.bonds: dict[int, dict[int, list[tuple[int, int]]]] = {}
        self.magnetic_structure: dict[str, any] = dict.fromkeys(magnetic_structure)
        self.spins = None
        self.time_evolution = None
        self.DSF = dict.fromkeys(dsf_data)
        
    def create_lattice(self, lattice_constants: triplet, super_cell: list[list[float]], size: tuple[int, int]) -> None:
        """
        Method for creating a lattice with given lattice constants (a, b, phi), where phi is the angle between
        the two lattice basis, and a super_cell (equivalently unit cell) containing the fractional coordinates
        of the spin sites inside the unit cell. "super_cell" is translated along the plane and integer
        number of times according to "size". The position of each spin site is contained in the "position" array,
        which will have a number of rows equal to the number of spin sites in the system, and two columns.
        """
        super_cell = np.asarray(super_cell)
        if np.any(super_cell >= 1):
            raise ValueError("Invalid fractional coordinates in super cell")

        a, b, phi = lattice_constants
        # The finite system contains MxN translated super_cells.
        M, N = size
        cell_sites: int = len(super_cell)
        super_cell = np.asarray(super_cell)

        # The position array is built by staking the translated super_cell to the initial position array.
        positions = np.zeros((cell_sites*M*N, 2))
        for i in range(M*N):
            m, n = i % M, i//M
            positions[cell_sites*i:cell_sites*(i + 1)] = super_cell + np.array([m, n])
                    
        positions = positions@np.array([[a, 0], [b*cos(phi), b*sin(phi)]])
        self.lattice["lattice_constants"] = lattice_constants
        self.lattice["super_cell"] = super_cell
        self.lattice["size"] = size
        self.lattice["positions"] = positions
        self.lattice["number_of_spins"]: int = positions.shape[0]

    def find_bonds(self, interval: tuple[float, float], boundary_conditions: str = "toroidal") -> None:
        """
        Method for creating bonds for spin sites whose distance is within the provided interval. The output is a
        dictionary that is indexed by increasing distance and then by increasing angle in the interval [0, pi).
        The method creates a temporary dictionary "bond_coordinates" that indexes bonds by their actual distance,
        and then by their actual angle. The distances and angles are sorted and used to enumerate the keys of the
        "bonds" dictionary.
        """
        positions = self.lattice["positions"]
        number_of_spins = self.lattice["number_of_spins"]
        M, N = self.lattice["size"]
        cell_sites: int = len(list(self.lattice["super_cell"]))

        def custom_arctan(vector: tuple[float, float]) -> float:
            """arctan that outputs in the range [0, pi)"""
            x, y = vector
            if y == 0:
                return 0

            elif y < 0:
                x, y = -x, -y

            return np.arctan2(y, x)

        bonds = {}
        bond_coordinates = {}
        min_distance, max_distance = interval

        # Finding bonds within the given interval for the first unit cell on the bottom left of the lattice
        for site1 in range(cell_sites):
            for site2 in range(site1+1, number_of_spins):
                distance = round(norm(positions[site2] - positions[site1]), 5)
                angle = round(custom_arctan(positions[site2] - positions[site1]), 5)
                if not (min_distance < distance <= max_distance):
                    continue

                elif distance not in bond_coordinates:
                    bond_coordinates[distance] = {angle: [(site1, site2)]}

                elif angle not in bond_coordinates[distance]:
                    bond_coordinates[distance][angle] = [(site1, site2)]

                else:
                    bond_coordinates[distance][angle].append((site1, site2))

        # Enumerating the bonds by increasing distance and then by increasing angle in [0, pi)
        for index, distance in enumerate(sorted(bond_coordinates)):
            for sub_index, angle in enumerate(sorted(bond_coordinates[distance])):
                bonds[index, sub_index] = bond_coordinates[distance][angle]

        for index, sub_index in bonds:
            new_bonds = []
            for site1, site2 in bonds[index, sub_index]:
                m0 = site2//cell_sites % M
                n0 = site2//(cell_sites*M) % N
                k0 = site2 % cell_sites
                for i in range(1, M*N):
                    m = i % M
                    n = i//M
                    if (m0 + m >= M or n0 + n >= N) and boundary_conditions == "open":
                        continue

                    elif n0 + n >= N and boundary_conditions == "cylindrical":
                        continue

                    m_new = (m + m0) % M
                    n_new = (n + n0) % N
                    new_site1 = site1 + i*cell_sites
                    new_site2 = k0 + m_new*cell_sites + n_new*cell_sites*M
                    new_bonds.append((new_site1, new_site2))

            bonds[index, sub_index] += new_bonds

        self.bonds = bonds
                    
    def couple(self, exchange_matrix, index: int, sub_index: int = None, color: str = 'k') -> None:
        """
        Method for adding spin exchange matrices to bonds found using 'find bonds'. The magnetic structure of the
        system is created/updated with the introduction of the exchange matrix.
        """

        number_of_spins = self.lattice["number_of_spins"]
        bonds = self.bonds
        adjacency_matrix = np.zeros((number_of_spins, number_of_spins))

        if sub_index is not None:
            for site1, site2 in bonds[index, sub_index]:
                adjacency_matrix[site1, site2] = 1

        else:
            for (i, sub_index) in bonds:
                if i != index:
                    continue

                for site1, site2 in bonds[index, sub_index]:
                    adjacency_matrix[site1, site2] = 1

        adjacency_matrix = adjacency_matrix + adjacency_matrix.T
        if self.magnetic_structure["adjacency_exchange_tensor"] is None:
            self.magnetic_structure["exchange_matrices"] = [exchange_matrix]
            self.magnetic_structure["adjacency_matrices"] = [adjacency_matrix]
            self.magnetic_structure["color"] = [color]
            self.magnetic_structure["adjacency_exchange_tensor"] = sp.sparse.kron(adjacency_matrix, exchange_matrix)

        else:
            self.magnetic_structure["exchange_matrices"].append(exchange_matrix)
            self.magnetic_structure["adjacency_matrices"].append(adjacency_matrix)
            self.magnetic_structure["color"].append(color)
            self.magnetic_structure["adjacency_exchange_tensor"] += sp.sparse.kron(adjacency_matrix, exchange_matrix)

    def random_spins(self) -> None:
        """Method for initializing random spins into the system"""
        if self.lattice is None:
            raise RuntimeError("System must have a lattice before initializing spins")

        number_of_spins = self.lattice["number_of_spins"]
        spins = np.zeros(3*number_of_spins)

        for i in range(number_of_spins):
            new_spin = np.random.multivariate_normal([0, 0, 0], np.eye(3))
            new_spin = new_spin/norm(new_spin)
            spins[3*i:3*(i+1)] = new_spin
            
        self.spins = spins
    
    def metropolis(self, number_of_steps: int, temperature: float) -> None:
        """Algorithm for sampling the lattice at a specific temperature."""

        if self.magnetic_structure["adjacency_exchange_tensor"] is None:
            raise RuntimeError("System must have a magnetic structure in order to use the metropolis algorithm.")

        print(f"Taking {number_of_steps:,} steps...")
        spins = self.spins
        number_of_spins = self.lattice["number_of_spins"]
        adjacency_exchange_tensor = self.magnetic_structure["adjacency_exchange_tensor"]
        external_field = self.magnetic_structure["external_field"]

        # All spins and random values are preloaded to minimize the action in the for loop.
        random_log_list = log(np.random.random(number_of_steps))
        random_sites = np.random.randint(number_of_spins, size=number_of_steps)
        # New (un-normalized) spins
        new_spins = np.random.multivariate_normal([0, 0, 0], np.eye(3), size=number_of_steps)
        adjacency_exchange_tensor = sp.sparse.csc_array(adjacency_exchange_tensor)

        pre_slice = []
        for i in range(number_of_spins):
            pre_slice.append(sp.sparse.coo_array(adjacency_exchange_tensor[3*i:3*(i+1),:]))

        pre_slice = np.asarray(pre_slice)
        if self.magnetic_structure["external_field"] is None:
            for step in range(number_of_steps):
                site = random_sites[step]
                new_spin = new_spins[step]/norm(new_spins[step])
                H_eff = pre_slice[site]@spins
                d_energy = np.dot(H_eff, new_spin-spins[3*site: 3*(site+1)])
                if temperature*random_log_list[step] < -d_energy:
                    spins[3*site: 3*(site+1)] = new_spin

                progress_bar(step, number_of_steps, 5000)

        else:
            for step in range(number_of_steps):
                site = random_sites[step]
                new_spin = new_spins[step]/norm(new_spins[step])
                H_eff = pre_slice[site]@spins - external_field
                d_energy = np.dot(H_eff, new_spin - spins[3*site:3*(site + 1)])
                if temperature * random_log_list[step] < -d_energy:
                    spins[3*site: 3*(site + 1)] = new_spin

                progress_bar(step, number_of_steps, 5000)

        self.spins = spins
        
    def simulated_annealing(self, number_of_steps: int, initial_temperature: float, alpha: float = 0) -> None:
        """
        Approximates the ground state of the system by use of simulated annealing.

        For each step, a spin site
        is picked at random and changed to a new random spin. The new spin is kept with probability
        p = exp(-delta_E/T), where T is the temperature at the given step in the algorithm, and delta_E is the
        difference in energy of the system before and after the spin is changed and is calculated using the effective
        field felt by the spin site. If the new spin is not kept, then the spin site is set to the normalized negative
        of the effective field to minimize the change in energy for the metropolis step.

        The method has the following annealing schedule: T(step) = T0*(1 - step/number_of_steps)^alpha. The annealing
        schedule is therefore controlled by setting the initial temperature, and alpha to determine how quickly the
        annealing temperature goes to 0.
        """

        if self.magnetic_structure["adjacency_exchange_tensor"] is None:
            raise RuntimeError("System must have a magnetic structure in order to use the metropolis algorithm.")

        print(f"Taking {number_of_steps:,} steps...")
        spins = self.spins
        number_of_spins = self.lattice["number_of_spins"]
        adjacency_exchange_tensor = self.magnetic_structure["adjacency_exchange_tensor"]
        external_field = self.magnetic_structure["external_field"]
        new_spins = np.random.multivariate_normal([0, 0, 0], np.eye(3), size=number_of_steps)

        # All spins and random values are preloaded to minimize the action in the for loop.
        random_log_list = log(np.random.random(number_of_steps))
        random_sites = np.random.randint(number_of_spins, size=number_of_steps)
        adjacency_exchange_tensor = sp.sparse.csc_array(adjacency_exchange_tensor)
        temperature = initial_temperature*(1 - np.arange(0, number_of_steps)/number_of_steps)**alpha

        pre_slice = []
        for i in range(number_of_spins):
            pre_slice.append(sp.sparse.coo_array(adjacency_exchange_tensor[3 * i:3 * (i + 1), :]))

        pre_slice = np.asarray(pre_slice)
        if self.magnetic_structure["external_field"] is None:
            for step in range(number_of_steps):
                site = random_sites[step]
                new_spin = new_spins[step]/norm(new_spins[step])
                H_eff = pre_slice[site]@spins
                d_energy = np.dot(H_eff, new_spin-spins[3*site: 3*(site+1)])
                if temperature[step]*random_log_list[step] < -d_energy:
                    spins[3*site: 3*(site+1)] = new_spin

                else:
                    spins[3*site:3*(site + 1)] = -H_eff/norm(H_eff)

        else:
            for step in range(number_of_steps):
                site = random_sites[step]
                new_spin = new_spins[step] / norm(new_spins[step])
                H_eff = pre_slice[site] @ spins - external_field
                d_energy = np.dot(H_eff, new_spin - spins[3 * site: 3 * (site + 1)])

                if temperature[step] * random_log_list[step] < -d_energy:
                    spins[3 * site: 3 * (site + 1)] = new_spin

                else:
                    spins[3 * site:3 * (site + 1)] = -H_eff / norm(H_eff)

        self.spins = spins

    def energy(self, print_energy: bool = True) -> float:
        """Method for determining the energy of the system."""

        if self.spins is None:
            raise RuntimeError("System does not have spins")

        number_of_spins = self.lattice["number_of_spins"]
        adjacency_exchange_tensor = self.magnetic_structure["adjacency_exchange_tensor"]
        spins = self.spins
        energy = 0.5*spins.T@adjacency_exchange_tensor@spins
        external_field = self.magnetic_structure["external_field"]

        if external_field is not None:
            spins = np.reshape(spins, (number_of_spins, 3))
            energy += -np.sum(spins@external_field)

        if print_energy:
            print(f"Energy: {energy}")

        return energy

    def flip(self, number_of_flips: int, print_spins: bool = False) -> None:
        """Method for creating random excitations in a system by flipping a number of its spins at random."""

        if self.spins is None:
            raise RuntimeError("System does not have spins to flip")

        number_of_spins = self.lattice["number_of_spins"]

        if number_of_spins < number_of_flips:
            raise ValueError("Desired number of spin flips is greater than the number of spins in the system.")

        spins = self.spins
        flip_list = []
        while len(flip_list) < number_of_flips:
            i = np.random.randint(number_of_spins)
            if i in flip_list:
                continue

            elif print_spins:
                print(f'Spin {i} was flipped')

            flip_list.append(i)
            flip = np.random.multivariate_normal([0, 0, 0], np.eye(3))
            flip = flip/norm(flip)
            spins[3*i:3*(i+1)] = flip

        self.spins = spins
        
    def LLG(self, dt: float, tf: float) -> None:

        if self.spins is None:
            raise RuntimeError("System does not have spins")

        print('Calculating spin time evolution...')
        number_of_spins = self.lattice["number_of_spins"]
        spins = self.spins
        time_steps = int(tf/dt)

        adjacency_matrices = np.asarray(self.magnetic_structure["adjacency_matrices"])
        exchange_matrices = np.asarray(self.magnetic_structure["exchange_matrices"])
        external_field = self.magnetic_structure["external_field"]
        if external_field is None:
            external_field = np.array([0, 0, 0])

        # noinspection PyUnreachableCode
        def EOM(t, state_vector):
            state_matrix = np.reshape(state_vector, (number_of_spins, 3))
            H_eff = np.sum(adjacency_matrices@state_matrix@exchange_matrices, axis=0)
            derivative = -np.cross(state_matrix, H_eff + external_field)
            return derivative.flatten()

        sol = integrate.solve_ivp(EOM, [0, tf], spins, t_eval=np.linspace(0, tf, time_steps))
        data = np.reshape(sol.y, (number_of_spins, 3, time_steps))
        self.time_evolution = (dt, tf, time_steps, data)
        print('Time evolution calculation finished')

    def print_lattice(self, hide_spins: bool = False, hide_bonds: bool = False, plot: bool = True, dpi: int = 200):

        """
            Method for plotting the spin system. The adjacency matrices of the system are used to plot the bonds
            between the spin sites. If no spins and/or adjacency matrices have been defined yet, only the lattice
            sites will be plotted.
        """
        number_of_spins = self.lattice["number_of_spins"]
        positions = self.lattice["positions"]
        adjacency_matrices = self.magnetic_structure["adjacency_matrices"]
        bond_color = self.magnetic_structure["color"]

        fig, ax = plt.subplots(dpi=dpi)
        ax.scatter(positions[:, 0], positions[:, 1], s=10)

        # Drawing the bonds between the paired spin sites
        if not hide_bonds and adjacency_matrices:
            for color, A in zip(bond_color, adjacency_matrices):
                i, j = np.nonzero(A)
                ax.plot([positions[i, 0], positions[j, 0]],
                        [positions[i, 1], positions[j, 1]], color=color, linewidth=1)

        # Drawing the spins of the systems
        spins = self.spins
        if spins is not None and not hide_spins:
            spins = np.reshape(self.spins, (number_of_spins, 3))
            quiv = ax.quiver(positions[:, 0], positions[:, 1], spins[:, 0], spins[:, 1],
                             scale=25, width=0.0025, angles="xy")

            # Adding the quiv to the axis for use in the animation method.
            ax.spin_plot = quiv

        x_max = max(positions[:, 0])+1.5
        x_min = min(positions[:, 0])-1.5
        y_max = max(positions[:, 1])+1.5
        y_min = min(positions[:, 1])-1.5
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        plt.xticks([], [])
        ax.set_xticks([])
        ax.set_xticks([], minor=True)
        plt.yticks([], [])
        ax.set_yticks([])
        ax.set_yticks([], minor=True)
        ax.set_aspect('equal', 'box')

        if plot:
            plt.show()

        return fig, ax
        
    def animate(self, path: str = None, **kwargs):
        """Method for animating the spin dynamics calculated by 'self.LLG()'"""

        if self.time_evolution is None:
            raise RuntimeError("Calculate time evolution before creating an animation")

        dt, tf, time_steps, data = self.time_evolution
        fig, ax = self.print_lattice(plot=False, **kwargs)
        # The quiver plot created by "self.print_lattice()" is stored as an attribute of the plt axis to be used here.
        quiv = ax.spin_plot

        def update(frame):
            quiv.set_UVC(data[:, 0, frame], data[:, 1, frame])
            return quiv

        ani = animation.FuncAnimation(fig=fig, func=update, frames=time_steps, interval=30)
        
        if path:
            ani.save(path, writer=animation.PillowWriter(fps=30))
            
        return ani
        
    def calculate_DSF(self, k_points: list[tuple[np.array, np.array]], steps: int = 200) -> None:
        if self.time_evolution is None:
            raise RuntimeError("Calculate time evolution before DSF calculation.")

        elif not k_points:
            raise ValueError("2 or more k points needed for path calculation.")

        print("Starting DSF path calculation...")

        positions = np.transpose(self.lattice["positions"])
        dt, tf, time_steps, data = self.time_evolution
        M, N = self.lattice["size"]
        nyquist_index = time_steps//2
        spins_z = data[:,2,:]
        kpoints_matrix = np.zeros((steps*len(k_points), 2))
        step_array = np.asarray([step/steps for step in range(steps)])

        for i, pair in enumerate(k_points):
            k0, k1 = pair
            kpoints_matrix[steps*i:steps*(i+1),:] = np.outer(step_array, k1 - k0) + k0

        DSF = np.abs(np.fft.fft(exp(-1j*kpoints_matrix@positions)@spins_z)[:, :nyquist_index])**2
        DSF = np.transpose(DSF)

        if np.max(DSF):
            DSF = DSF/np.max(DSF)

        print('DSF path calculation finished')
        self.DSF = (steps, k_points, DSF)

    def plot_DSF(self, labels: list[str], y_max: float = 3, label=None, plot: bool = True, **kwargs):
        if self.DSF is None:
            raise RuntimeError("Cannot plot dynamical structure factor before DSF calculation.")

        dt, tf, time_steps, data = self.time_evolution
        steps, k_points, DSF = self.DSF

        if labels and (len(labels) != len(k_points)+1):
            raise ValueError("Number of labels provided do not match the number of k points")

        Q: list[float] = []
        step_array = np.asarray([step/steps for step in range(steps)])
        for i, pair in enumerate(k_points):
            k1, k0 = pair
            dk = norm(k1 - k0)/steps
            if i == 0:
                Q = [dk*step for step in range(steps)]
                continue

            Q += [Q[-1] + dk*step for step in range(steps)]

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_ylim([0, y_max])
        
        if labels:
            for i in range(1, len(labels)-1):
                plt.axvline(x=Q[steps*i], color='w')

        my_xticks = [Q[steps*i] for i in range(len(labels)-1)]
        my_xticks.append(Q[-1])
        plt.xticks(my_xticks, labels)
        omega = np.arange(0, 1/(2*dt), 1/tf)*2*pi
        c = ax.pcolormesh(Q, omega, DSF, **kwargs)
        plt.ylabel(r'$\omega$')
        fig.colorbar(c, ax=ax, ticks=None, label=label)

        if plot:
            plt.show()

        return fig, ax

    def sample_DSF(self, number_of_samples: int) -> callable:
        def decorator(function: callable) -> callable:
            def wrapper(*args, **kwargs) -> np.array:
                averaged_DSF = sum(serial_computation(function, number_of_samples))/number_of_samples
                steps, kpoint_path, _ = self.DSF
                self.DSF = (steps, kpoint_path, averaged_DSF)
                return averaged_DSF
            return wrapper
        return decorator
