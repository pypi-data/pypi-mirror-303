
from itertools import product
from typing import List, Union

import numpy as np
from spglib import niggli_reduce

from mgtoolbox_kernel.util.base import (get_lattice_parameters,
                                        get_lattice_vectors)


class Cell(object):
    """
    表示晶体晶格的类。

    该类用于存储和操作晶体晶格的参数和基矢。
    """

    def __init__(self, a: float, b: float, c: float, alpha: float, beta: float, gamma: float, cell_basis_vectors=None):
        """
        初始化晶体晶格。

        :param a: 晶格参数 a
        :param b: 晶格参数 b
        :param c: 晶格参数 c
        :param alpha: 晶格角度 alpha
        :param beta: 晶格角度 beta
        :param gamma: 晶格角度 gamma
        :param cell_basis_vectors: 晶格基矢，默认为 None
        """
        
        self._cell_param: np.ndarray = np.zeros((2, 3))
        self._cell_param[0] = [a, b, c]
        self._cell_param[1] = [alpha, beta, gamma]
        # self._cell_basis_vectors = None
        if cell_basis_vectors is None:
            self.__set_cell_basis_vectors(a, b, c, alpha, beta, gamma)
        else:
            self._cell_basis_vectors = cell_basis_vectors

    def __eq__(self, other: 'Cell') -> bool:
        return self is other or np.allclose(self._cell_basis_vectors, other._cell_basis_vectors)

    def __repr__(self) -> str:
        cstring = {
            'lattice': self._cell_basis_vectors,
            'parameters': self._cell_param.reshape(6, )
        }
        return str(cstring)

    @property
    def abc(self) -> np.ndarray:
        """Get the cell parameters:a,b,c

        Returns
        -------
        np.ndarray
            cell parameters:a,b,c
        """
        return self._cell_param[0]

    @abc.setter
    def abc(self, value):
        self._cell_param[0] = value

    @property
    def angles(self) -> np.ndarray:
        """Get the cell parameters:alpha,beta,gamma

        Returns
        -------
        numpy.ndarray
            cell parameters:alpha,beta,gamma
        """
        return self._cell_param[1]

    @angles.setter
    def angles(self, value: Union[np.ndarray, List]):
        self._cell_param[1] = value

    @property
    def lattice_parameters(self):
        return np.hstack((self.abc, self.angles))

    @property
    def cell_basis_vectors(self):
        return self._cell_basis_vectors

    @property
    def volume(self):
        return np.fabs(np.linalg.det(np.transpose(self.cell_basis_vectors)))

    @property
    def reciprocal_cell_vectors(self):
        '''获取倒易晶格向量，不包括2pi的系数

        Returns
        -------
            倒易晶格向量
        '''
        return np.transpose(np.linalg.pinv(self.cell_basis_vectors))

    def __set_cell_basis_vectors(self, a, b, c, alpha, beta, gamma):
        self._cell_basis_vectors = get_lattice_vectors(a, b, c, alpha, beta, gamma)

    @staticmethod
    def from_lattice_parameters(a, b, c, alpha, beta, gamma):
        return Cell(a, b, c, alpha, beta, gamma)

    @staticmethod
    def from_cell_vectors(cell_vectors: np.ndarray, fix_cell_vectors: bool = False):
        (a, b, c, alpha, beta, gamma) = get_lattice_parameters(cell_vectors)
        if not fix_cell_vectors:
            return Cell(a, b, c, alpha, beta, gamma)
        else:
            return Cell(a, b, c, alpha, beta, gamma, cell_vectors)

    def get_distances(
            self,
            cart_coords1,
            cart_coords2=None,
            mic=True
    ):
        """Get the minimum distance of to list of cartesian coordinates

        Parameters
        ----------
        list | numpy.ndarray
            cartesian coordinates
        list | numpy.ndarray, optional
            cartesian coordinates, by default None

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            minimum image distance vectors and its distances
        """
        pbc = [True, True, True]
        cart_coords1 = np.array(cart_coords1)
        if cart_coords2 is None:
            n1 = len(cart_coords1)
            # upper triangular index
            i1, i2 = np.triu_indices(n1, k=1)
            distances_vecters = cart_coords1[i2] - cart_coords1[i1]
        else:
            cart_coords2 = np.array(cart_coords2)
            distances_vecters = (cart_coords2[np.newaxis, :, :] - cart_coords1[:, np.newaxis, :]).reshape((-1, 3))

        if np.sum(pbc) == 0 or mic == False:
            minimum_vecters = np.asarray(distances_vecters)
            vector_lengths = np.linalg.norm(distances_vecters, axis=1)
        else:
            minimum_vecters, vector_lengths = self.__find_mic_distances(distances_vecters)

        if cart_coords2 is None:
            Dout = np.zeros((n1, n1, 3))
            Dout[(i1, i2)] = minimum_vecters
            Dout -= np.transpose(Dout, axes=(1, 0, 2))

            Dout_len = np.zeros((n1, n1))
            Dout_len[(i1, i2)] = vector_lengths
            Dout_len += Dout_len.T
            return Dout, Dout_len

        minimum_vecters.shape = (-1, len(cart_coords2), 3)
        vector_lengths.shape = (-1, len(cart_coords2))

        return minimum_vecters, vector_lengths

    def __find_mic_distances(self, vecters):
        """Get the minimum image distance of each atoms

        Parameters
        ----------
        numpy.ndarray
            distance vectors

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            minimum image distance vectors and its distances
        """
        pbc = [True, True, True]
        n = np.sum(pbc)
        minimum_vecters = []
        vector_lengths = []
        for v in vecters:
            mic_flag = False
            if n == 3:
                minimum_vecter, vector_length = self.__direct_find_mic(v)
                if (vector_length < 0.5 * min(self.abc)):
                    mic_flag = True
                    minimum_vecters.append(minimum_vecter)
                    vector_lengths.append(vector_length)
                    continue
                else:
                    mic_flag = False
                    minimum_vecters = []
                    vector_lengths = []
                    break
        minimum_vecters = np.array(minimum_vecters)
        vector_lengths = np.array(vector_lengths)
        if not mic_flag:
            minimum_vecters, vector_lengths = self.__reduce_find_mic(vecters)

        return minimum_vecters, vector_lengths

    def __direct_find_mic(self, vecter):
        """Calculate the minimum image distances,and use the result when the minimum image convention is satisfied.The minimum image convention i.e distance < min(a,b,c)/2

        Parameters
        ----------
        numpy.ndarray
            distance vector

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            minimum image distance vector and its distance
        """
        # convert to fractional coordinates
        frac_coord = self.get_fractional_coordinates(vecter)
        # Control the fractional coordinate range to (-0.5,0.5)
        frac_coord -= np.floor(frac_coord + 0.5)
        minimum_vecter = self.get_cartesian_coords(frac_coord)
        vector_length = np.linalg.norm(minimum_vecter)
        # Returns the shortest vector and its length
        return minimum_vecter, vector_length

    def __reduce_find_mic(self, vecters):

        """If the minimum image convention is not satisfied, reduce the cell to re-calculate the minimum image distances

        Parameters
        ----------
        vecters : numpy.ndarray
            distance vectors

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            minimum image distance vectors and its distances
        """
        pbc = [True, True, True]
        cart_coords = self.__wrap_atoms(vecters)
        # set the periodic range of three vector directions according to the periodic boundary conditions. (-1,1)
        periodic_range = [np.arange(-1 * p, p + 1) for p in pbc]
        hkl_range = list(product(*periodic_range))
        vecter_range = np.dot(hkl_range, self.cell_basis_vectors)
        # get all atoms' coordinates in the cell and its mirror cells
        expanded_cart_coords = cart_coords + vecter_range[:, None]
        # calculate the minimum image distance and get its index
        lengths = np.linalg.norm(expanded_cart_coords, axis=2)
        indices = np.argmin(lengths, axis=0)
        minimum_vecters = expanded_cart_coords[indices, np.arange(len(cart_coords)), :]
        vector_lengths = lengths[indices, np.arange(len(cart_coords))]
        return minimum_vecters, vector_lengths

    def __wrap_atoms(self, cart_coord):
        """If there is periodicity in this direction, wrap the specified component of the coordinate into the cell
        Parameters
        ----------
        numpy.ndarray
            cartesian coordinate

        Returns
        -------
        numpy.ndarray
            cartesian coordinate
        """
        pbc = [True, True, True]
        frac_coord = self.get_fractional_coordinates(cart_coord)
        for i, periodic in enumerate(pbc):
            if periodic:
                frac_coord[:, i] %= 1.0
        return self.get_cartesian_coords(frac_coord)

    def distance(self, coord1, coord2=None, mic: bool = True):
        """Get the minimum distance of to list of cartesian coordinates

        Parameters
        ----------
        coord1 : list | numpy.ndarray
            笛卡尔坐标
        coord2 : list | numpy.ndarray
            笛卡尔坐标，by default None，即coord1为距离向量
        mic : bool
            最小像距离，by default True

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            最小像距离向量，向量长度
        """
        if coord2 is None:
            distance_vector = np.array(coord1)
        else:
            cart_coord1 = np.array(coord1)
            cart_coord2 = np.array(coord2)
            distance_vector = cart_coord2 - cart_coord1
        if not mic:
            minimum_vector = distance_vector
            vector_length = np.linalg.norm(minimum_vector)
        else:
            minimum_vector, vector_length = self.find_mic_distance(distance_vector)
        return minimum_vector, vector_length

    def find_mic_distance(self, vector: np.ndarray):
        """Get the minimum image distance of specific two sites

        Parameters
        ----------
        vector : numpy.ndarray
            距离向量

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            minimum image distance vector and its distance
        """
        minimum_vector, vector_length = self.direct_find_mic(vector)
        if vector_length < 0.5 * min(self.abc):
            mic_flag = True
        else:
            mic_flag = False
        minimum_vector = np.array(minimum_vector)
        vector_length = np.array(vector_length)
        if not mic_flag:
            minimum_vector, vector_length = self.reduce_find_mic(vector)
        return minimum_vector, vector_length

    def direct_find_mic(self, vector: np.ndarray):
        """Calculate the minimum image distances,and use the result when the minimum image convention is satisfied.The minimum image convention i.e distance < min(a,b,c)/2

        Parameters
        ----------
        vector : numpy.ndarray
            距离向量

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            minimum image distance vector and its distance
        """

        # convert to fractional coordinates
        frac_coord = self.get_fractional_coordinates(vector)
        # Control the fractional coordinate range to (-0.5,0.5)
        frac_coord -= np.floor(frac_coord + 0.5)
        minimum_vector = self.get_cartesian_coords(frac_coord)
        vector_length = np.linalg.norm(minimum_vector)
        # Returns the shortest vector and its length
        return minimum_vector, vector_length

    def reduce_find_mic(self, vector: np.ndarray):
        """If the minimum image convention is not satisfied, reduce the cell to re-calculate the minimum image distance

        Parameters
        ----------
        vector : numpy.ndarray
            距离向量

        Returns
        -------
        numpy.ndarray, numpy.ndarray
            minimum image distance vectors and its distances
        """
        pbc = [True, True, True]
        cart_coord = self.wrap_atoms(vector)
        # set the periodic range of three vector directions according to the periodic boundary conditions. (-1,1)
        periodic_range = [np.arange(-1 * p, p + 1) for p in pbc]
        hkl_range = list(product(*periodic_range))
        vector_range = np.dot(hkl_range, self.cell_basis_vectors)
        # get all atoms' coordinates in the cell and its mirror cells
        expanded_cart_coords = []
        for v in vector_range:
            expanded_cart_coords.append(cart_coord + v)
        # calculate the minimum image distance and get its index
        lengths = np.linalg.norm(expanded_cart_coords, axis=1)
        index = np.argmin(lengths, axis=0)
        minimum_vector = expanded_cart_coords[index]
        vector_length = lengths[index]
        return np.array(minimum_vector), np.array(vector_length)

    def wrap_atoms(self, cart_coord):
        """If there is periodicity in this direction, wrap the specified component of the coordinate into the cell

        Parameters
        ----------
        cart_coord : numpy.ndarray
            cartesian coordinate

        Returns
        -------
        numpy.ndarray
            cartesian coordinate
        """
        pbc = [True, True, True]
        frac_coord = self.get_fractional_coordinates(cart_coord)
        for i, periodic in enumerate(pbc):
            if periodic:
                frac_coord[i] %= 1.0
        return self.get_cartesian_coords(frac_coord)

    def get_reduced_cell(self, algorithm: str = 'niggli'):
        """Select the reduce algorithm to reduce the cell,i.e,1.niggli 2.minkowski

        Parameters
        ----------
        algorithm : str, optional
            choose, by default 'niggli'

        Returns
        -------
        Cell
            the Cell object after reduced
        """
        if algorithm == 'niggli':
            new_cell_vectors = niggli_reduce(self._cell_basis_vectors)
        else:
            new_cell_vectors = self._cell_basis_vectors
        return self.from_cell_vectors(new_cell_vectors)

    def get_cartesian_coords(self, frac_coords: np.ndarray) -> np.ndarray:
        """get_cartesian_coords 从分数坐标得到笛卡尔坐标

        Parameters
        ----------
        frac_coords : np.ndarray
            分数坐标

        Returns
        -------
        np.ndarray
            笛卡尔坐标
        """
        return np.dot(frac_coords, self.cell_basis_vectors)

    def get_fractional_coordinates(self, cart_coords: np.ndarray) -> np.ndarray:
        """get_Fractional_coordinates 从笛卡尔坐标得到分数坐标

        Parameters
        ----------
        cart_coords : np.ndarray
            笛卡尔坐标

        Returns
        -------
        np.ndarray
            分数坐标
        """
        return np.dot(cart_coords, np.linalg.inv(self.cell_basis_vectors))
