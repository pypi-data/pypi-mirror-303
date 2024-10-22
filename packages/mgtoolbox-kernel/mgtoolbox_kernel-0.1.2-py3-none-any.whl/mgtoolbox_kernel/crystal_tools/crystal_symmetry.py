from typing import List, Dict
from spglib import get_symmetry_dataset
import numpy as np
from mgtoolbox_kernel.kernel import Structure,SymmetryStructure


def get_symm_ops(struct:Structure):
    """
    获取结构的对称性操作。
    通过使用spglib库来获取给定结构的空间群操作,包括旋转和平移操作。

    参数:
    struct:Structure - 一个Structure对象,包含了晶体结构信息。

    返回:
    rot - 旋转操作的数组。
    trans - 平移操作的数组。
    """
    lattice = struct.cell.cell_basis_vectors.tolist()
    # 获取结构的分数坐标列表
    positions = [site.coord for site in struct.sites]
    sites_str_list, mapping_number = get_site_type_mapping(struct.sites)
    numbers = [mapping_number[i] for i in sites_str_list]
    spglib_cell = (lattice, positions, numbers)
    try:
        symmetry_dataset = get_symmetry_dataset(spglib_cell, symprec = 0.01, angle_tolerance = 5.0)
        rot = symmetry_dataset.get('rotations')
        trans = symmetry_dataset.get('translations')
    except:
        # 未能正确读取空间群信息的默认为空间群P1的操作
        rot = np.array([[ 1,  0,  0],
                        [ 0,  1,  0],
                        [ 0,  0,  1]]),
        trans = np.array([0.,0.,0.])
    return rot, trans

def get_space_group_info(struct:Structure) -> Dict:
    space_group_info = {}
    lattice = struct.cell.cell_basis_vectors.tolist()
    # 获取结构的分数坐标列表
    positions = [site.coord for site in struct.sites]
    sites_str_list, mapping_number = get_site_type_mapping(struct.sites)
    numbers = [mapping_number[i] for i in sites_str_list]
    spglib_cell = (lattice, positions, numbers)
    try:
        symmetry_dataset = get_symmetry_dataset(spglib_cell, symprec = 0.01, angle_tolerance = 5.0)
        space_group_info['space_group_number'] = symmetry_dataset.get('number')
        space_group_info['space_group_name'] = symmetry_dataset.get('international')
        space_group_info['space_group_hall_number'] = symmetry_dataset.get('hall_number')
    except:
        # 未能正确读取空间群信息的默认为P1
        space_group_info['space_group_number'] = 1
        space_group_info['space_group_name'] = 'P1'
        space_group_info['space_group_hall_number'] = 1
    return space_group_info

    
def get_site_type_mapping(sites: List, consider_site_features=True):
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

if __name__ == "__main__":
    stru3 = Structure.from_file(r"D:\warehouses\cavd\examples\cifs\Li\icsd_16713.cif")
    stru2 = SymmetryStructure.from_file("../../examples/icsd_58.cif")
    stru1 = SymmetryStructure.from_file(r"D:\warehouses\cavd\examples\cifs\Li\icsd_16713.cif")
    rot, trans = get_symm_ops(stru2)
    rot, trans = get_symm_ops(stru3)
    print(rot)