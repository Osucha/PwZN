import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from rich.progress import Progress
import matplotlib
matplotlib.use("Agg")  # backend bez wyświetlania okienka bo inaczej rzuca błąd

from numba import njit

@njit
def calculate_energy(grid, i, j, J, B, grid_size):
    neighbors = (
        grid[(i+1) % grid_size, j] +
        grid[(i-1) % grid_size, j] +
        grid[i, (j+1) % grid_size] +
        grid[i, (j-1) % grid_size]
    )
    return -J * grid[i, j] * neighbors - B * grid[i, j]

@njit
def flip_spin(grid, i, j, J, B, beta, grid_size):
    delta_E = -2 * calculate_energy(grid, i, j, J, B, grid_size)
    if delta_E < 0 or np.random.rand() < np.exp(-delta_E * beta):
        grid[i, j] *= -1

class IsingSimulation:
    def __init__(self, grid_size, J, beta, B, steps, spin_density=0.5, img_prefix=None, anim_file=None, mag_file=None):
        self.grid_size = grid_size
        self.J = J
        self.beta = beta
        self.B = B
        self.steps = steps
        self.img_prefix = img_prefix
        self.anim_file = anim_file
        self.mag_file = mag_file
        self.grid = np.random.choice([1, -1], size=(grid_size, grid_size), p=[spin_density, 1 - spin_density])
        self.magnetization = []
        self.grids = []

    # @njit
    # def _energy(self, i, j):
    #     neighbors = self.grid[(i+1) % self.grid_size, j] + self.grid[(i-1) % self.grid_size, j] + \
    #                 self.grid[i, (j+1) % self.grid_size] + self.grid[i, (j-1) % self.grid_size]
    #     return -self.J * self.grid[i, j] * neighbors - self.B * self.grid[i, j]

    # @njit
    # def _flip_spin(self, i, j):
    #     delta_E = -2 * self._energy(i, j)
    #     if delta_E < 0 or np.random.rand() < np.exp(-delta_E * self.beta):
    #         self.grid[i, j] *= -1

    def run(self):
        with Progress() as progress:
            task = progress.add_task("Running simulation...", total=self.steps)
            for step in range(self.steps):
                for _ in range(self.grid_size ** 2):
                    i, j = np.random.randint(0, self.grid_size, size=2)
                    # self._flip_spin(i, j)
                    flip_spin(self.grid, i, j, self.J, self.B, self.beta, self.grid_size)
                self.magnetization.append(np.sum(self.grid))
                self.grids.append(self.grid.copy())
                if self.img_prefix:
                    self._save_image(step)
                progress.update(task, advance=1)

        if self.anim_file:
            fig, ax = plt.subplots()
            im = ax.imshow(self.grids[0], cmap='coolwarm', animated=True)

            def update(frame):
                im.set_array(frame)
                return [im]

            ani = FuncAnimation(fig, update, frames=self.grids, blit=True, interval=100)
            ani.save(self.anim_file, writer='imagemagick')
            
        if self.mag_file:
            self._save_magnetization()

    def _save_image(self, step):
        plt.imshow(self.grid, cmap='coolwarm')
        plt.axis('off')
        plt.savefig(f".\pngs\{self.img_prefix}_{step}.png")
        plt.close()

    def _save_magnetization(self):
        with open(self.mag_file, 'w') as f:
            for m in self.magnetization:
                f.write(f"{m}\n")

def main():
    parser = argparse.ArgumentParser(description="2D Ising Model Simulation")
    parser.add_argument("--grid_size", type=int, default=20, help="Size of the grid (NxN)")
    parser.add_argument("--J", type=float, default=1.0, help="Interaction parameter J")
    parser.add_argument("--beta", type=float, default=0.5, help="Inverse temperature (beta)")
    parser.add_argument("--B", type=float, default=0.0, help="External magnetic field (B)")
    parser.add_argument("--steps", type=int, default=100, help="Number of simulation steps")
    parser.add_argument("--spin_density", type=float, default=0.5, help="Initial density of up spins")
    parser.add_argument("--img_prefix", type=str, help="Prefix for image files (optional)")
    parser.add_argument("--anim_file", type=str, help="File name for animation output (optional)")
    parser.add_argument("--mag_file", type=str, help="File name for magnetization data output (optional)")

    args = parser.parse_args()

    # Run the simulation with parsed arguments
    sim = IsingSimulation(
        grid_size=args.grid_size,
        J=args.J,
        beta=args.beta,
        B=args.B,
        steps=args.steps,
        spin_density=args.spin_density,
        img_prefix=args.img_prefix,
        anim_file=args.anim_file,
        mag_file=args.mag_file
    )
    sim.run()

if __name__ == "__main__":
    main()
