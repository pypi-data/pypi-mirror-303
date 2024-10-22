import numpy as np
from scipy.interpolate import RegularGridInterpolator


class PotentialField(object):

    def __init__(
        self,
        Potential: np.ndarray,
        basis_vector: np.ndarray = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    ) -> None:
        self.potential = Potential
        self.compute_gradients()
        self.create_interpolat_function()
        self.basis_vector: np.ndarray = np.array([[1, 0, 0], [0, 1, 0],
                                                  [0, 0, 1]])

    def create_interpolat_function(self):
        data_shape = self.potential.shape
        x = np.linspace(0, 1, data_shape[0])
        y = np.linspace(0, 1, data_shape[1])
        z = np.linspace(0, 1, data_shape[2])
        self.potential_interp_function = RegularGridInterpolator(
            (x, y, z), self.potential)
        self.potential_gradients_interp_function_x = RegularGridInterpolator(
            (x, y, z), self.potential_gradients[0][:][:][:])
        self.potential_gradients_interp_function_y = RegularGridInterpolator(
            (x, y, z), self.potential_gradients[1][:][:][:])
        self.potential_gradients_interp_function_z = RegularGridInterpolator(
            (x, y, z), self.potential_gradients[2][:][:][:])

    def compute_gradients(self):
        self.potential_gradients = np.gradient(self.potential)

    def get_gradients(self, coords: np.ndarray):
        return np.array([
            self.potential_gradients_interp_function_x(coords),
            self.potential_gradients_interp_function_y(coords),
            self.potential_gradients_interp_function_z(coords)
        ])

    def get_potentials(self, coords: np.ndarray):
        return self.potential_interp_function(coords)


class PeriodPotentialField(PotentialField):

    def __init__(
        self,
        Potential: np.ndarray,
        basis_vector: np.ndarray = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    ) -> None:
        super().__init__(Potential, basis_vector)

    def compute_gradients(self):
        super().compute_gradients()
        # period boundary condtion
        self.potential_gradients[0][ 0][ :][ :] \
            = (-self.potential[-2][ :][ :] + self.potential[1][ :][ :]) * 0.5
        self.potential_gradients[0][ -1][ :][ :] \
            = (-self.potential[-2][ :][ :] + self.potential[1][ :][ :]) * 0.5
        self.potential_gradients[1][ :][ 0][ :] \
            = (-self.potential[:][ -2][ :] + self.potential[:][ 1][ :]) * 0.5
        self.potential_gradients[1][ :][ -1][ :] \
            = (-self.potential[:][ -2][ :] + self.potential[:][ 1][ :]) * 0.5
        self.potential_gradients[2][ :][ :][ 0] \
            = (-self.potential[:][ :][ -2] + self.potential[:][ :][ 1]) * 0.5
        self.potential_gradients[2][ :][ :][ -1] \
            = (-self.potential[:][ :][ -2] + self.potential[:][ :][ 1]) * 0.5

    def get_gradients(self, coords: np.ndarray):
        fcoords = np.mod(coords, 1.0)
        result = np.array([
            self.potential_gradients_interp_function_x(fcoords)[0],
            self.potential_gradients_interp_function_y(fcoords)[0],
            self.potential_gradients_interp_function_z(fcoords)[0]
        ])
        return result

    def get_potentials(self, coords: np.ndarray):
        return self.potential_interp_function(np.mod(coords, 1.0))
