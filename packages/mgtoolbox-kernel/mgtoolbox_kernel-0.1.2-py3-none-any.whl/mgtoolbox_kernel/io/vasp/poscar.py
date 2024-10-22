# -*- encoding: utf-8 -*-
"""
    @File    :   poscar.py
    @Time    :   2022/01/12 08:56:01
    @Author  :   何冰 
    @Version :   0.1
    @Email   :   shhebing@qq.com
    @WebSite :   https://mtoolbox.cn
    @Desc    :   Read vasp,poscar file convert to structure model
"""
import sys
from pathlib import Path
from typing import List

import numpy as np
import spglib as spg

from mgtoolbox_kernel.util.base import get_lattice_parameters


class PoscarParse(object):
    def __init__(self, filename=None):
        self.structure: dict = {}
        self.poscar_string: str = ""
        self.lattice_vectors: np.ndarray = np.zeros((3, 3))
        self.sites: List = []
        if filename:
            self.read_file(filename)

    def read_file(self, filename: str):
        vaspfile = Path(filename)
        with vaspfile.open() as f:
            self.__poscar_lines_list = f.readlines()
        self.__parse(self.__poscar_lines_list)

    def __parse(self, poscar_lines: List[str]):
        lines = poscar_lines
        self.comment = lines[0].strip()
        scale = float(lines[1].split()[0])
        if scale < 0:
            scale = 1.0

        self.lattice_vectors[0] = scale * np.array(
            [float(x) for x in lines[2].split()[0:3]]
        )
        self.lattice_vectors[1] = scale * np.array(
            [float(x) for x in lines[3].split()[0:3]]
        )
        self.lattice_vectors[2] = scale * np.array(
            [float(x) for x in lines[4].split()[0:3]]
        )
        self.natoms_list = np.array([int(x) for x in lines[5].split() if x.isdigit()])
        self.species_list = None
        self.natom_of_species = {}
        self.site_species_list = []
        if self.natoms_list.size == 0:
            self.species_list = [x for x in lines[5].split()]
            self.natoms_list = np.array(
                [int(x) for x in lines[6].split() if x.isdigit()]
            )
            for i, key in enumerate(self.species_list):
                self.natom_of_species[key] = self.natoms_list[i]
                self.site_species_list += [key] * self.natoms_list[i]
        natoms = np.sum(self.natoms_list)
        if self.species_list is None:
            raise ValueError("Not supported the file format")
        coord_mode = lines[7]
        current_line = 7
        if coord_mode[0].lower() in ["s"]:
            current_line += 1
            coord_mode = lines[current_line]
        self.coord_type = None
        if coord_mode[0].lower() in ["c", "k"]:
            self.coord_type = "Cartesian"
        elif coord_mode[0].lower() in ["d"]:
            self.corrd_type = "Direct"
        self.coords = np.zeros((natoms, 3))
        for i in range(natoms):
            current_line += 1
            self.coords[i] = [float(x) for x in lines[current_line].split()[0:3]]

    def get_structure(self):
        structure = {}
        try:
            structure["lattice_parameters"] = self.__get_lattice_parameter()
            structure["sites"] = self.__get_sites()
            structure["symm_ops"] = self.__get_symm_ops()
            structure["oxidation_state"] = None
            structure['attributes'] = None
        except KeyError as e:
            sys.stderr.write(str(e) + "\n")
            return None
        return structure

    def __get_lattice_parameter(self):
        return get_lattice_parameters(self.lattice_vectors)

    def __get_sites(self):
        sites = []
        label_id = 0
        current_species = ""
        for i, item in enumerate(self.coords):
            site = {}
            if current_species != self.site_species_list[i]:
                label_id = 1
            site["label"] = self.site_species_list[i] + str(label_id)
            site["site_type"] = self.site_species_list[i]
            site["coord"] = item
            site["occupancy"] = {self.site_species_list[i]: 1.0}
            sites.append(site)
            label_id += 1
            current_species = self.site_species_list[i]
        return sites

    def __get_symm_ops(self):
        spgroup = spg.get_symmetry_from_database(1)
        return spgroup["rotations"], spgroup["translations"]


if __name__ == "__main__":
    ciff = PoscarParse()
    ciff.read_file("./devtest/vasptest.vasp")
    structs = [ciff.get_structure()]
    print(len(structs))
    for struct in structs:
        print(struct["symm_ops"][0])
        print(struct["symm_ops"][1])
        print(
            spg.get_hall_number_from_symmetry(
                struct["symm_ops"][0], struct["symm_ops"][1], symprec=1e-5
            )
        )
