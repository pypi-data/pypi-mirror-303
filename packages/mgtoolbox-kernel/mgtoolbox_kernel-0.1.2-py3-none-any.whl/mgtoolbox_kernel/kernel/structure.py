# -*- encoding: utf-8 -*-
"""
    @File    :   structure.py
    @Time    :   2021/04/30 15:49:14
    @Author  :   何冰 
    @Email   :   shhebing@qq.com
    @WebSite :   https://mgtoolbox.cn
    @Desc    :   材料结构相关类。
"""
import re
from typing import Dict, List, Union
from pathlib import Path
from itertools import product

from collections import OrderedDict
import numpy as np
import scipy.spatial
from spglib import get_symmetry_dataset
from mgtoolbox_kernel.io import read_structure_file, read_structure_data
from .mgclass import MGobject
from .atom import Atom
from .cell import Cell
from .site import Site


class Structure(MGobject):
    def __init__(self, sites: List[Site], cell: Cell, attributes=None):
        if attributes is None:
            attributes = {}
        super().__init__(attributes)
        self.sites: List[Site] = sites
        self.cell: Cell = cell

    def __repr__(self) -> str:
        sstring = str({"cell": self.cell, "sites": self.sites})
        return sstring

    def add_site(self, site: Site):
        self.sites.append(site)

    def add_sites(self, sites: List[Site]):
        self.sites += sites

    def remove_sites(self, sites: List[Site]):
        for site in sites:
            self.sites.remove(site)

    def set_cell(self, cell: Cell):
        self.cell = cell

    @property
    def is_ordered(self):
        """是否为有序结构

        Returns
        -------
        bool
            是否有序
        """
        return all((site.is_ordered for site in self.sites))

    @staticmethod
    def from_file(filename: Union[str, Path]) -> Union["Structure", List["Structure"]]:
        structs_mode = read_structure_file(filename)
        structs = []
        for struct_mode in structs_mode:
            struct = Structure.from_struct_model(struct_mode)
            structs.append(struct)
        if len(structs) == 1:
            return structs[0]
        else:
            return structs

    @staticmethod
    def from_data(file_data: str):
        # 默认cif格式文件数据
        structs_mode = read_structure_data(file_data)
        structs = []
        for struct_mode in structs_mode:
            struct = Structure.from_struct_model(struct_mode)
            structs.append(struct)
        if len(structs) == 1:
            return structs[0]
        else:
            return structs

    @staticmethod
    def merge_eq_coords(coords):
        Structure.adjust_coords(coords)
        dm = scipy.spatial.distance_matrix(coords, coords)
        type_list = list(range(dm.shape[0]))
        for row in range(dm.shape[0]):
            for col in range(row + 1, dm.shape[1]):
                if dm[row][col] < 0.003:
                    type_list[col] = type_list[row]
        unique_ids = set(type_list)
        ucoords = coords[list(unique_ids)]
        return ucoords

    @staticmethod
    def adjust_coords(coords):
        """调整分数坐标值
        使得分数坐标值在0.999-1.001范围的坐标更改为0.0
        Parameters
        ----------
        coords : _type_
            _description_
        """
        abs_value = np.abs(coords - 1.0)
        coords[abs_value < 0.001] = 0.0

    @staticmethod
    def from_struct_model(struct_mode: Dict):
        lattice_paramteters = struct_mode["lattice_parameters"]
        cell = Cell(
            lattice_paramteters[0],
            lattice_paramteters[1],
            lattice_paramteters[2],
            lattice_paramteters[3],
            lattice_paramteters[4],
            lattice_paramteters[5],
        )
        attributes = struct_mode['attributes']
        sites = []
        for struct_site in struct_mode["sites"]:
            coords = np.mod(
                np.dot(struct_mode["symm_ops"][0], struct_site["coord"])
                + struct_mode["symm_ops"][1],
                1.0,
            )
            # 合并等价位点中坐标相同位点
            # Merge the points with the same coordinates in the equivalent points
            ucoords = Structure.merge_eq_coords(coords)
            for i, coord in enumerate(ucoords):
                occupier = {}
                for symbol, occupy in struct_site["occupancy"].items():
                    if occupy < 0.0:
                        raise ValueError("Structure file site occupy value error")
                    sym = re.findall(r"[A-Z][a-z]?", symbol)
                    if struct_mode["oxidation_state"]:
                        atom = Atom(sym[0], struct_mode["oxidation_state"][symbol])
                        occupier[atom] = occupy
                    else:
                        # -16 表示该离子化合价无法确定。
                        atom = Atom(sym[0], -16)
                        occupier[atom] = occupy
                site = Site(coord, occupier)
                site.label = struct_site["label"] + "_" + str(i)
                site.type = struct_site["site_type"]
                sites.append(site)
        unique_sites = Structure.remove_duplicates_sites(sites)
        return Structure(unique_sites, cell, attributes)

    @staticmethod
    def remove_duplicates_sites(sites: List[Site]):
        result = []
        for item in sites:
            if item not in result:
                result.append(item)
            else:
                result[result.index(item)].assign_occupier_by_dict(item.occupier)
        return result

    def write_to_cif(self, filename: str):
        with Path(filename).open("+w") as f:
            f.write(f"data_{Path(filename).stem}\n")

            f.write("_cell_length_a       {}\n".format(self.cell.abc[0]))
            f.write("_cell_length_b       {}\n".format(self.cell.abc[1]))
            f.write("_cell_length_c       {}\n".format(self.cell.abc[2]))

            f.write("_cell_angle_alpha    {}\n".format(self.cell.angles[0]))
            f.write("_cell_angle_beta     {}\n".format(self.cell.angles[1]))
            f.write("_cell_angle_gamma    {}\n".format(self.cell.angles[2]))

            f.write("_symmetry_space_group_name_H-M    'P 1'\n")
            f.write("_symmetry_Int_Tables_number        1\n")

            f.write("loop_\n")
            f.write("_symmetry_equiv_pos_site_id\n")
            f.write("_symmetry_equiv_pos_as_xyz\n")
            f.write("1        'x, y, z'\n")

            f.write("loop_\n")
            f.write("_atom_site_label\n")
            f.write("_atom_site_type_symbol\n")
            f.write("_atom_site_fract_x\n")
            f.write("_atom_site_fract_y\n")
            f.write("_atom_site_fract_z\n")
            f.write("_atom_site_occupancy\n")
            for site in self.sites:
                for occupier, occupy in site.occupier.items():
                    f.write(
                        f"{site.label} {occupier.symbol} {site.x} {site.y} {site.z} {occupy}\n"
                    )

            f.write(f"#End of data_{Path(filename).stem}")

    def get_mic_dis(self, fracoord1, fracoord2):
        """
        Considering the periodicity of crystals to obtain the distance
        between two points within the crystal.
        :param fracoord1: fractional coordinates of site frac_site1,such as[0.5, 0.5, 0.5]
        :param fracoord2: fractional coordinates of site frac_site2
        :return: the shortest distance between two sites
        """
        pbc = [True, True, True]
        periodic_range = [np.arange(-1 * p, p + 1) for p in pbc]
        hkl_range = list(product(*periodic_range))
        lattice_matrix = self.cell.cell_basis_vectors
        actual_site1 = np.dot(fracoord1, lattice_matrix)
        fracoord2 = np.array(fracoord2)
        dis_list = []
        for i in hkl_range:
            period_i = np.array(i)
            temp_frac_site2 = period_i + fracoord2
            temp_actual_site2 = np.dot(temp_frac_site2, lattice_matrix)
            temp_dis = np.linalg.norm(temp_actual_site2 - actual_site1)
            dis_list.append(temp_dis)
        sorted_list = sorted(dis_list)
        min_dis = sorted_list[0]
        # max_value = min_dis + 0.03
        # cout = 0
        # for num in sorted_list:
        #     if min_dis <= num <= max_value:
        #         cout += 1
        return min_dis
        
class SymmetryStructure(Structure):
    def __init__(self, sites: List[Site], cell: Cell, space_group_info: Dict, symm_ops, attributes=None):
        if attributes is None:
            attributes = {}
        super().__init__(sites, cell, attributes)
        self.space_group_info: Dict = space_group_info
        self.symm_ops = symm_ops

    def __repr__(self) -> str:
        sstring = str({"cell": self.cell, "sites": self.sites})
        return sstring

    def add_site(self, site: Site):
        self.sites.append(site)

    def add_sites(self, sites: List[Site]):
        self.sites += sites

    def remove_sites(self, sites: List[Site]):
        for site in sites:
            self.sites.remove(site)

    def set_cell(self, cell: Cell):
        self.cell = cell

    @property
    def is_ordered(self):
        """是否为有序结构

        Returns
        -------
        bool
            是否有序
        """
        return all((site.is_ordered for site in self.sites))

    @staticmethod
    def from_file(filename: Union[str, Path]) -> Union["Structure", List["Structure"]]:
        structs_mode = read_structure_file(filename)
        structs = []
        for struct_mode in structs_mode:
            struct = SymmetryStructure.from_struct_model(struct_mode)
            structs.append(struct)
        if len(structs) == 1:
            return structs[0]
        else:
            return structs

    @staticmethod
    def from_data(file_data: str):
        # 默认cif格式文件数据
        structs_mode = read_structure_data(file_data)
        structs = []
        for struct_mode in structs_mode:
            struct = SymmetryStructure.from_struct_model(struct_mode)
            structs.append(struct)
        if len(structs) == 1:
            return structs[0]
        else:
            return structs

    @staticmethod
    def from_struct_model(struct_mode: Dict):
        symm_ops = struct_mode["symm_ops"]
        lattice_paramteters = struct_mode["lattice_parameters"]
        cell = Cell(
            lattice_paramteters[0],
            lattice_paramteters[1],
            lattice_paramteters[2],
            lattice_paramteters[3],
            lattice_paramteters[4],
            lattice_paramteters[5],
        )
        attributes = struct_mode['attributes']
        sites = []
        for struct_site in struct_mode["sites"]:
            coords = np.mod(
                np.dot(struct_mode["symm_ops"][0], struct_site["coord"])
                + struct_mode["symm_ops"][1],
                1.0,
            )
            # 合并等价位点中坐标相同位点
            # Merge the points with the same coordinates in the equivalent points
            ucoords = Structure.merge_eq_coords(coords)
            # 若存在磁矩信息则读取
            magmoms = []
            magcoords = []
            if 'magmoms' in attributes:
                if struct_site["label"] in attributes['magmoms']:
                    magmom = attributes['magmoms'].get(struct_site["label"], np.array([0, 0, 0]))
                    for mag_rot, mag_trans, mag_t in attributes['mag_symopts']:
                        magmoms.append(np.dot(mag_rot, magmom) * np.linalg.det(mag_rot))
                        magcoords.append(np.mod(np.dot(struct_site['coord'], mag_rot) + mag_trans, 1.0).reshape(3,))
            for i, coord in enumerate(ucoords):
                occupier = {}
                for symbol, occupy in struct_site["occupancy"].items():
                    if occupy < 0.0:
                        raise ValueError("Structure file site occupy value error")
                    sym = re.findall(r"[A-Z][a-z]?", symbol)
                    if struct_mode["oxidation_state"]:
                        if struct_mode["oxidation_state"][symbol]:
                            atom = Atom(sym[0], struct_mode["oxidation_state"][symbol])
                            occupier[atom] = occupy
                        else:
                            atom = Atom(sym[0], -16)
                            occupier[atom] = occupy
                    else:
                        # -16 表示该离子化合价无法确定。
                        atom = Atom(sym[0], -16)
                        occupier[atom] = occupy
                site = Site(coord, occupier)
                site.label = struct_site["label"] + "_" + str(i)
                site.type = struct_site["site_type"]
                if len(magcoords) > 0:
                    idx = None
                    for ii, arr in enumerate(magcoords):
                        if np.array_equal(arr, coord):
                            idx = ii
                            break
                    if idx is not None:
                        site.attributes['magmom'] = magmoms[idx]
                sites.append(site)
        unique_sites = Structure.remove_duplicates_sites(sites)
        space_group_info = SymmetryStructure.get_space_group_info(cell, unique_sites)
        nonequivalent_site_index = np.unique(space_group_info['equivalent_atoms'])
        nonequivalent_site = [unique_sites[index] for index in nonequivalent_site_index]
        return SymmetryStructure(nonequivalent_site, cell, space_group_info, symm_ops, attributes)
    
    def get_space_group_info(cell: Cell, sites: List[Site]):
        space_group_info = {}
        # 获取spglib格式晶胞以及站点与原子序号的映射字典，如{1:[3],2:[3],3:[8]...}
        lattice = cell.cell_basis_vectors.tolist()    
        # 获取结构的分数坐标列表
        positions = [site.coord for site in sites]
        sites_str_list, mapping_number = SymmetryStructure.get_site_type_mapping(sites)
        numbers = [mapping_number[i] for i in sites_str_list]
        # magmoms = None
        spglib_cell = (lattice, positions, numbers)
        try:
            symmetry_dataset = get_symmetry_dataset(spglib_cell, symprec = 0.01, angle_tolerance = 5.0)
            space_group_info['space_group_number'] = symmetry_dataset.get('number')
            space_group_info['space_group_name'] = symmetry_dataset.get('international')
            space_group_info['space_group_hall_number'] = symmetry_dataset.get('hall_number')
            space_group_info['equivalent_atoms'] = symmetry_dataset.get('equivalent_atoms')
        except:
            # 未能正确读取空间群信息的默认为P1
            space_group_info['space_group_number'] = 1
            space_group_info['space_group_name'] = 'P1'
            space_group_info['space_group_hall_number'] = 1
            space_group_info['equivalent_atoms'] = np.arange(0,len(sites))
        return space_group_info

    def get_site_type_mapping(sites: List[Site], consider_site_features=True):
        # 根据该站点的元素符号，原子占据率，原子化合价判断是否为相同类型的站点
        sites_str_list = []  # 列表中元素为:元素符号_原子占据率_化合价['Li_1.0_0.0',...]
        for site in sites:
            atom_symbols = sorted(site.atom_symbols)
            atom_occupancies = sorted(site.atom_occupancies)
            atom_valences = sorted(site.atom_valences)
            symbols = "".join(symbol + '_' for symbol in atom_symbols)
            occupancy = ""
            valence = ""
            magmom = "0"
            if consider_site_features:
                occupancy = "".join([str(occ) + '_' for occ in atom_occupancies])
                valence = "".join([str(val) + '_' for val in atom_valences])
                if 'magmom' in site.attributes:
                    magnetic_moment = site.attributes['magmom']
                else:
                    magnetic_moment = 0
                magmom = str(magnetic_moment).replace(' ', '')
            site_symbol_occu_valence_str = symbols + occupancy + valence + magmom
            sites_str_list.append(site_symbol_occu_valence_str)
        mapping_number = {}  # 存储对应字符串映射的序号，标识不同类型站点
        n = 0
        for s in sites_str_list:
            if s not in mapping_number.keys():
                n += 1
                mapping_number[s] = n
        return sites_str_list, mapping_number
        
    def write_to_cif(self, filename: str):
        with Path(filename).open("+w") as f:
            f.write(f"data_{Path(filename).stem}\n")

            f.write("_cell_length_a       {}\n".format(self.cell.abc[0]))
            f.write("_cell_length_b       {}\n".format(self.cell.abc[1]))
            f.write("_cell_length_c       {}\n".format(self.cell.abc[2]))

            f.write("_cell_angle_alpha    {}\n".format(self.cell.angles[0]))
            f.write("_cell_angle_beta     {}\n".format(self.cell.angles[1]))
            f.write("_cell_angle_gamma    {}\n".format(self.cell.angles[2]))

            f.write("_symmetry_space_group_name_H-M    'P 1'\n")
            f.write("_symmetry_Int_Tables_number        1\n")

            f.write("loop_\n")
            f.write("_symmetry_equiv_pos_site_id\n")
            f.write("_symmetry_equiv_pos_as_xyz\n")
            f.write("1        'x, y, z'\n")

            f.write("loop_\n")
            f.write("_atom_site_label\n")
            f.write("_atom_site_type_symbol\n")
            f.write("_atom_site_fract_x\n")
            f.write("_atom_site_fract_y\n")
            f.write("_atom_site_fract_z\n")
            f.write("_atom_site_occupancy\n")
            for site in self.sites:
                for occupier, occupy in site.occupier.items():
                    f.write(
                        f"{site.label} {occupier.symbol} {site.x} {site.y} {site.z} {occupy}\n"
                    )

            f.write(f"#End of data_{Path(filename).stem}")
    
    def write_to_poscar(self, filename: str, scale: float = 1.0):
        """
        根据SymmetryStructure生成POSCAR文件。

        参数：
        filename (str): 要写入的POSCAR文件名。
        scale (float): 比例因子,默认为1.0。
        返回：
        无。
        """
        if self.is_ordered:
            lattice_matrix = [
                [self.cell.abc[0], 0.0, 0.0],
                [0.0, self.cell.abc[1], 0.0],
                [0.0, 0.0, self.cell.abc[2]],
            ]
            # elements (list): 包含元素符号的列表。例如，['O', 'Si', 'Si', 'O']
            elements = [site.atom_symbols[0] for site in self.sites]
            unique_elements = []
            element_counts = []
            # 统计元素出现次数
            for element in elements:
                if unique_elements and unique_elements[-1] == element:
                    element_counts[-1] += 1
                else:
                    unique_elements.append(element)
                    element_counts.append(1)
            element_counts = list(map(str, element_counts))
            # symbols (list): 包含化合价的离子列表。例如， ['Li+', 'Li+', 'Li+', 'Li+', 'Sc3+']
            symbols = []
            # frac_coords (list): 包含原子坐标的三维列表。每个原子应该有三个浮点坐标，格式为[[x1, y1, z1], [x2, y2, z2], ...]
            frac_coords = []
            for site in self.sites:
                ionic = site.atom_symbols[0]
                valence = site.atom_valences[0]
                ion_symbol = get_ion_symbol(ionic, valence)
                symbols.append(ion_symbol)
                frac_coords.append(site.coord)
            # 统计每种元素的数量
            count_dict = OrderedDict()
            for elem in elements:
                count_dict[elem] = count_dict.get(elem, 0) + 1
            # 创建元素和数量的组合列表
            lst = [f"{key}{value}" for key, value in count_dict.items()]
            try:
                # 打开文件进行写入
                with open(filename, "w") as f:
                    # 写入晶体名称
                    f.write(" ".join(lst) + "\n")
                    # 写入比例因子
                    f.write("{:.8f}\n".format(scale))
                    # 写入晶格向量，转换为A单位
                    np.savetxt(f, np.array(lattice_matrix) * scale, fmt='%.6f')
                    # 写入元素符号
                    f.write(" ".join(unique_elements) + "\n")
                    # 写入每种元素的数量
                    f.write(" ".join(element_counts) + "\n")
                    # 指定坐标系类型为Direct
                    f.write("Direct\n")
                    # 写入原子坐标和对应的元素符号
                    for frac_coord, symbol in zip(frac_coords, symbols):
                        f.write(" ".join(f"{v:.6f}" for v in frac_coord) + " " + symbol + "\n")
            except Exception as e:
                # 捕获并打印写入文件的错误
                print(f"Error writing to file {filename}: {e}")
        else:
            raise ValueError("Structure with partial occupancies cannot be " "converted into POSCAR!")
def get_ion_symbol(ionic, valence):
    """
    生成含化合价的离子，如 Li+。

    参数：
    ionic (str): 元素符号，如 Li。
    valence (int): 化合价

    返回: 含化合价的离子，如 Li+
    """
    valence = int(valence)
    
    if valence == 0:
        return ionic  # 如果化合价为0，返回元素符号
    
    sign = '+' if valence > 0 else '-'
    
    # 当化合价为1时，不显示数字
    if abs(valence) == 1:
        return f"{ionic}{sign}"
    
    return f"{ionic}{abs(valence)}{sign}"
