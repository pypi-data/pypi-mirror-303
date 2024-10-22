# -*- encoding: utf-8 -*-
'''
    @File    :   cif.py
    @Time    :   2021/12/1
    @Author  :   何冰 
    @Email   :   shhebing@qq.com
    @WebSite :   https://mtoolbox.cn
    @Desc    :   cif文件处理相关类。
'''
import sys
from typing import List, Union, Dict
import numpy as np
from scipy.spatial import distance_matrix
import spglib as spg
from CifFile import ReadCif, get_number_with_esd
from mgtoolbox_kernel.util.base import parse_sitesym

spacegroup_to_hall_number = [
    0, 1, 2, 3, 6, 9, 18, 21, 30, 39, 57, 60, 63, 72, 81, 90, 108, 109, 112,
    115, 116, 119, 122, 123, 124, 125, 128, 134, 137, 143, 149, 155, 161, 164,
    170, 173, 176, 182, 185, 191, 197, 203, 209, 212, 215, 218, 221, 227, 228,
    230, 233, 239, 245, 251, 257, 263, 266, 269, 275, 278, 284, 290, 292, 298,
    304, 310, 313, 316, 322, 334, 335, 337, 338, 341, 343, 349, 350, 351, 352,
    353, 354, 355, 356, 357, 358, 359, 361, 363, 364, 366, 367, 368, 369, 370,
    371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385,
    386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400,
    401, 402, 404, 406, 407, 408, 410, 412, 413, 414, 416, 418, 419, 420, 422,
    424, 425, 426, 428, 430, 431, 432, 433, 435, 436, 438, 439, 440, 441, 442,
    443, 444, 446, 447, 448, 449, 450, 452, 454, 455, 456, 457, 458, 460, 462,
    463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477,
    478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492,
    493, 494, 495, 497, 498, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509,
    510, 511, 512, 513, 514, 515, 516, 517, 518, 520, 521, 523, 524, 525, 527,
    529, 530
]


class CifFileParse(object):

    def __init__(self):
        self._structures = []

    def read_file(self, filename):
        cif_file = ReadCif(filename, scantype='flex')
        for cif_struct in cif_file:
            structure = self.__get_structure(cif_struct)
            if structure:
                self._structures.append(structure)

    def get_structures(self) -> List[Dict[str, Union[str, float]]]:
        return self._structures

    def __get_lattice_parameter(self, cif_struc):
        cell = np.zeros(6, )
        cell[0] = get_number_with_esd(cif_struc['_cell_length_a'])[0]
        cell[1] = get_number_with_esd(cif_struc['_cell_length_b'])[0]
        cell[2] = get_number_with_esd(cif_struc['_cell_length_c'])[0]
        cell[3] = get_number_with_esd(cif_struc['_cell_angle_alpha'])[0]
        cell[4] = get_number_with_esd(cif_struc['_cell_angle_beta'])[0]
        cell[5] = get_number_with_esd(cif_struc['_cell_angle_gamma'])[0]
        return cell

    def __get_symm_ops(self, cif_struc):
        if '_symmetry_equiv_pos_as_xyz' in cif_struc:
            return self.__parse_sitesym(
                cif_struc['_symmetry_equiv_pos_as_xyz'])
        elif '_symmetry_Int_Tables_number' in cif_struc:
            spgnumber = int(cif_struc['_symmetry_Int_Tables_number'])
            spgroup = spg.get_symmetry_from_database(
                spacegroup_to_hall_number[spgnumber])
            return spgroup['rotations'], spgroup['translations']
        elif '_space_group_IT_number' in cif_struc:
            spgnumber = int(cif_struc['_space_group_IT_number'])
            spgroup = spg.get_symmetry_from_database(
                spacegroup_to_hall_number[spgnumber])
            return spgroup['rotations'], spgroup['translations']
        else:
            # 若以上参数结构文件中都不包含，默认为'x,y,z'
            return self.__parse_sitesym(['x,y,z'])

    def __get_oxidation(self, cif_struc):
        oxi = {}
        if '_atom_type_oxidation_number' not in cif_struc:
            return None
        for i, key in enumerate(cif_struc['_atom_type_symbol']):
            oxi[key] = float(cif_struc['_atom_type_oxidation_number'][i])
        return oxi

    def __get_sites(self, cif_struc):
        sites = []
        for i, item in enumerate(cif_struc['_atom_site_label']):
            site = {}
            site['label'] = item
            site['site_type'] = cif_struc['_atom_site_type_symbol'][i]
            x = get_number_with_esd(cif_struc['_atom_site_fract_x'][i])[0]
            y = get_number_with_esd(cif_struc['_atom_site_fract_y'][i])[0]
            z = get_number_with_esd(cif_struc['_atom_site_fract_z'][i])[0]
            site['coord'] = np.array([x, y, z])
            site['occupancy'] = {
                cif_struc['_atom_site_type_symbol'][i]:
                get_number_with_esd(cif_struc['_atom_site_occupancy'][i])[0]
            }
            sites.append(site)

        return self.__merge_sites(sites)

    def __merge_sites(self, sites):
        site_no = self.__get_coord_eq_sites(sites)
        unique_no = set(site_no)
        unique_sites = []
        for uno in unique_no:
            unique_sites.append(sites[uno])
            unique_sites[-1]['site_type'] = uno
            for i in range(len(site_no)):
                if (uno == site_no[i]) and uno != i:
                    for k, v in sites[i]['occupancy'].items():
                        unique_sites[-1]['occupancy'][k] = v
        return unique_sites

    def __get_coord_eq_sites(self, sites: list):
        sites_coords = np.array([coord['coord'] for coord in sites])
        dm = distance_matrix(sites_coords, sites_coords)
        type = list(range(dm.shape[0]))
        for row in range(dm.shape[0]):
            for col in range(row + 1, dm.shape[1]):
                if dm[row][col] < 0.0001:
                    type[col] = type[row]
        return type

    def __parse_sitesym(self, symlist, sep=','):
        return parse_sitesym(symlist,sep)

    def __get_attributes(self, cif_struc):
        attr = {}
        if '_chemical_formula_sum' in cif_struc:
            formula = cif_struc['_chemical_formula_sum']
        elif '_chemical_formula_structural' in cif_struc:
            formula = cif_struc['_chemical_formula_structural']
        elif '_chemical_formula_moiety' in cif_struc:
            formula = cif_struc['_chemical_formula_moiety']
        else:
            formula = None
        attr['chemical_formula'] = formula
        return attr

    def __get_structure(self, cif_struc):
        structure = {}
        try:
            structure['lattice_parameters'] = self.__get_lattice_parameter(
                cif_struc)
            structure['sites'] = self.__get_sites(cif_struc)
            structure['symm_ops'] = self.__get_symm_ops(cif_struc)
            structure['oxidation_state'] = self.__get_oxidation(cif_struc)
            structure['attributes'] = self.__get_attributes(cif_struc)
        except (KeyError) as e:
            sys.stderr.write(str(e) + '\n')
            return None
        return structure
