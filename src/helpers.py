from typing import Callable, NamedTuple
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt

# Default graph sizes:
w = 10
h = w/2


class SizesType(NamedTuple):
    rect = (w, h)
    quad = (w, w)


class SolutionEval:
    def __init__(self,
                 sigma_fn: Callable[[float], float],
                 omeganull_fn: Callable[[float], float],
                 eval_range: tuple[float, float, float]):
        """Utility class to easily evaluate a 'Naeherungsloesung'.

        Args:
            sigma_fn (Callable[[float], float]): Function to calculate sigma.
            omeganull_fn (Callable[[float], float]): Function to calculate omega_null
            eval_range (tuple[float, float, float]): Tuple representing a range (start, stop, step) to evaluate the solutions.
        """
        self._sigma_fn: Callable[[float], float] = sigma_fn
        self._omega_null_fn: Callable[[float], float] = omeganull_fn
        self._range = np.arange(*eval_range)

    def sigma(self, x):
        return self._sigma_fn(x)

    def omega_null(self, x):
        return self._omega_null_fn(x)

    def ranged_sigma(self):
        return np.array([self.sigma(x) for x in self._range])

    def ranged_omega(self):
        return np.array([self.omega(x) for x in self._range])

    def ranged_omega_null(self):
        return np.array([self.omega_null(x) for x in self._range])

    def omega(self, x):
        return self._omega_null_fn(x) * cmath.cos(self.epsilon(x))

    def epsilon(self, x):
        return cmath.asin(self._sigma_fn(x)/self._omega_null_fn(x))


sizes = SizesType

deg2rad = math.pi / 180
rad2deg = 1/deg2rad


def plot_single_value(subplot, x, solution: SolutionEval, show_epsilon=False):
    fig, ax = subplot
    sigma = '%.4f' % solution._sigma_fn(x)
    omega = '%.4f' % solution.omega(x).real
    epsilon = '%.2f' % (solution.epsilon(x).real * rad2deg)
    if show_epsilon:
        ax.plot([0, solution._sigma_fn(x).real], [0, solution.omega(x).real],
                color='red')
    ax.plot([0, solution._sigma_fn(x).real], [
            0, solution.omega(x).real], color='red', linestyle='None', marker='x',
            label=f'$\sigma={sigma}$\n$\omega={omega}$\n$\epsilon={epsilon}$')
    fig.legend(loc='upper center')


def plot_complex(subplot, x, y):
    fig, ax = subplot
    ax.plot(x, y)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position(('axes', 1))
    ax.spines['bottom'].set_position(('data', 0))
    ax.set_ylim([0, max(y)])
    ax.set_xlim([min(x), 0])
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_ylabel('Kreisfrequenz ($j\omega$)')
    ax.set_xlabel('Dämpfung ($\sigma$)')
    plt.grid(True)
    return fig, ax
