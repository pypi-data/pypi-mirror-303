# -*- encoding: utf-8 -*-
"""
    @File    :   ionic_radius.py
    @Time    :   2024/10/1
    @Author  :   赖智聪
    @Version :   0.1
    @Email   :   3338910983@qq.com
    @Desc    :   晶体结构分析。
"""
from collections import OrderedDict
import numpy as np
from CifFile import ReadCif
from cavd.modules import ionic_radiianalysis
from cavd.modules.oxidation_state import get_oxstate_from_struct
from cavd.netstorage import AtomNetwork
from mgtoolbox_kernel.kernel.structure import Structure, SymmetryStructure


def get_struct_radii(filename, migrant, rad_flag, rad_dict):
    """
    根据文件名和其他参数获取结构和半径信息,并判断cif文件中是否存在迁移离子

    参数:
    - filename: 字符串，表示结构文件的路径。
    - migrant: 字符串，表示迁移的离子符号。
    - rad_flag: 布尔值，表示是否需要计算半径。
    - rad_dict: 字典，表示预先定义的半径字典。

    返回值:
    - struct: SymmetryStructure对象,表示从文件中读取的结构。
    - radii: 字典，表示根据条件获取的半径信息。
    """
    struct = SymmetryStructure.from_file(filename)
    is_ion_in_struct(struct, migrant)
    radii = {}
    if rad_flag:
        if rad_dict:
            radii = rad_dict
        else:
            radii = get_radii_from_struct(struct)
    return struct, radii
    
def get_skestruct_radii(filename, migrant, rad_flag, rad_dict):
    """
    根据给定的晶体结构文件和其他参数，返回结构对象和半径字典。

    参数:
    - filename: str晶体结构文件的路径。
    - migrant: 该参数未在函数中使用，可能是为未来功能预留。
    - rad_flag: bool指示是否需要计算或提供原子半径的标志。
    - rad_dict: dict包含原子半径信息的字典,如果为None则使用默认半径。
    
    返回:
    - struct: SymmetryStructure,读取并可能经过处理的晶体结构对象。
    - radii: dict,包含原子半径的字典。
    """
    struct = SymmetryStructure.from_file(filename)
    # 如果结构中位点无化合价信息，则计算位点化合价
    if struct.sites[0].atom_valences[0] == -16:
        oxstate = get_oxstate_from_struct(struct)
    radii = {}
    if rad_flag:
        if rad_dict:
            radii = rad_dict
        else:
            radii = get_radii_from_struct(struct)
    return struct, radii
def get_dis_periods(p1, p2, abc, angles):
    """
    p1,p2为分数坐标
    abc,angles为晶胞常数
    """
    dis, cout = ionic_radiianalysis.get_period_dis(p1, p2, abc, angles)
    return dis


def get_radii_from_struct(struct: Structure):
    radii = ionic_radiianalysis.get_ionicradius(struct)
    return radii


def get_radii(filename):
    structs = Structure.from_file(filename)
    radii = ionic_radiianalysis.get_ionicradius(structs)
    return radii


def is_ion_in_struct(struct: Structure, migrant):
    elements = []
    for i in struct.sites:
        if i.atom_symbols[0] not in elements:
            elements.append(i.atom_symbols[0])
    if migrant not in elements:
        raise ValueError(
            "The input migrant ion not in the input structure! Please check it."
        )


def is_ion_in_material(filename, migrant):
    structs = Structure.from_file(filename)
    elements = []
    for i in structs.sites:
        if i.atom_symbols[0] not in elements:
            elements.append(i.atom_symbols[0])
    if migrant not in elements:
        raise ValueError(
            "The input migrant ion not in the input structure! Please check it."
        )


def get_sym_opt(filename):
    cif_file = ReadCif(filename, scantype="flex")
    for cif_struct in cif_file:
        sitesym = cif_struct["_symmetry_equiv_pos_as_xyz"]
    return sitesym


def get_spacegroups_number_sybol(filename):
    cif_file = ReadCif(filename, scantype="flex")
    for cif_struct in cif_file:
        symm_number = cif_struct["_symmetry_int_tables_number"]
        symm_sybol = cif_struct["_symmetry_space_group_name_h-m"]
    return symm_number, symm_sybol


def localEnvirCom(stru, migrant):
    ioniccoord = ionic_radiianalysis.get_ioniccoord(stru)
    coord_tmp = []
    nei_dis_tmp = []
    min_nei_dis_tmp = []
    migrant_paras = []
    migrant_radii = []

    for key in ioniccoord:
        if migrant in key:
            nearest_ion = ioniccoord[key][2][0]
            nearest_ion_radii = ioniccoord[nearest_ion][1]
            nei_dis = ioniccoord[key][2][1]
            alpha_tmp = (nei_dis - nearest_ion_radii) / ioniccoord[key][1]
            coord_tmp.append(ioniccoord[key][0])
            nei_dis_tmp.append(nei_dis)
            min_nei_dis_tmp.append(nei_dis - nearest_ion_radii)
            migrant_paras.append(alpha_tmp)
            migrant_radii.append(nearest_ion_radii)
    nei_dises = list(zip(coord_tmp, zip(nei_dis_tmp, min_nei_dis_tmp)))
    migrant_alpha = float(sum(migrant_paras)) / len(migrant_paras)
    if migrant_alpha > 1.0:
        migrant_alpha = 1.0
    migrant_radius = float(sum(migrant_radii)) / len(migrant_radii)
    return migrant_radius, migrant_alpha, nei_dises


# Analyze the relationships between mobile ions and their coordination ions.
def localEnvirCom_new(stru, migrant):
    """
    分析给定结构中移动离子的局部环境信息。

    参数:
    - stru: 晶体结构，用于获取离子的配位信息。
    - migrant: 需要分析的迁移离子。

    返回:
    一个元组列表，依次为迁移离子的配位数以及到最近邻离子的距离和考虑到最近邻离子半径的表面距离。
    """
    ioniccoord = ionic_radiianalysis.get_ioniccoord(stru)
    coord_tmp = []
    nei_dis_tmp = []
    surf_nei_dis_tmp = []
    for key, value in ioniccoord.items():  # 使用.items()进行迭代
        if migrant in key:
            coord_tmp.append(value[0])
            nei_dis_tmp.append(value[2][1])
            nearest_ion = value[2][0]
            nearest_ion_radii = ioniccoord[nearest_ion][1]
            surf_nei_dis_tmp.append(value[2][1] - nearest_ion_radii)
    nei_dises = list(zip(coord_tmp, zip(nei_dis_tmp, surf_nei_dis_tmp)))

    return nei_dises


def get_ion_symbol(ionic, valence):
    """
    生成含化合价的离子如Li+。

    参数：
    ionic (str): 元素符合,如Li。
    valence (int): 化合价

    返回: 含化合价的离子如Li+

    """
    valence = int(valence)
    if valence == 1:
        ion_symbol = ionic + "+"
        return ion_symbol

    elif valence == -1:
        ion_symbol = ionic + "-"
        return ion_symbol

    ion_symbol = ionic + str(abs(valence)) + ("- " if valence < 0 else "+")
    return ion_symbol


def get_poscar_para(stru):

    # elements (list): 包含元素符号的列表。例如，['O', 'Si', 'Si', 'O']
    elements = [site.atom_symbols[0] for site in stru.sites]

    # symbols (list): 包含化合价的离子列表。例如， ['Li+', 'Li+', 'Li+', 'Li+', 'Sc3+']
    symbols = []

    # frac_coords (list): 包含原子坐标的三维列表。每个原子应该有三个浮点坐标，格式为[[x1, y1, z1], [x2, y2, z2], ...]
    frac_coords = []
    for site in stru.sites:
        ionic = site.atom_symbols[0]
        valence = site.atom_valences[0]
        ion_symbol = get_ion_symbol(ionic, valence)
        symbols.append(ion_symbol)
        frac_coords.append(site.coord)
    lattice = stru.cell.abc
    # lattice_matrix (list): 三维列表，包含晶体格矢量。每个格矢量应包含三个浮点数
    lattice_matrix = [
        [lattice[0], 0.0, 0.0],
        [0.0, lattice[1], 0.0],
        [0.0, 0.0, lattice[2]],
    ]
    return lattice_matrix, frac_coords, elements, symbols


def write_poscar(filename, stru, scale=1.0):
    """
    生成POSCAR文件。

    参数：
    filename (str): 要写入的POSCAR文件名。
    stru: 材料结构
    scale (float): 比例因子,默认为1.0。

    返回：
    无。

    """

    lattice_matrix, frac_coords, elements, symbols = get_poscar_para(stru)

    # 确定原子总数和每种元素的数量
    count_dict = OrderedDict()
    for i in elements:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    keys_lst = list(count_dict.keys())
    values_lst = list(count_dict.values())
    # 将 values_lst 中的整型元素转换成字符串类型
    values_str_lst = list(map(str, values_lst))

    lst = []
    for key, value in count_dict.items():
        lst.append(key + str(value))

    # 打开文件进行写入
    with open(filename, "w") as f:
        # 写入晶体名称
        f.write(" ".join(lst) + "\n")

        # 写入比例因子
        f.write("{:.8f}\n".format(scale))

        # 写入晶格向量，并转换为A单位
        for vector in np.array(lattice_matrix) * scale:
            f.write(" ".join(["{:.6f}".format(v) for v in vector]) + "\n")

        # 写入元素符号和数量
        f.write(" ".join(keys_lst) + "\n")
        f.write(" ".join(values_str_lst) + "\n")

        # 写入坐标系类型
        f.write("Direct\n")

        # 写入原子坐标
        for frac_coord, symbol in zip(frac_coords, symbols):
            f.write(
                " ".join(["{:.6f}".format(v) for v in frac_coord]) + " " + symbol + "\n"
            )

def struct_to_AtomNetwork(cif_struct:SymmetryStructure, ionradii_dict:dict)->AtomNetwork:
    """
    将给定的晶体结构对象转换为原子网络对象。
    
    参数:
    cif_struct: SymmetryStructure类型的晶体结构对象,包含晶格和原子信息。
    
    返回:
    AtomNetwork类型的对象,包含转换后的原子网络信息。
    """
    atmnet=AtomNetwork()
    atmnet.lattice_para=cif_struct.cell.abc
    atmnet.lattice_angle=cif_struct.cell.angles
    atoms = []
    for site in cif_struct.sites:
        if site.atom_symbols[0] != "Li":
            cart_coord = np.dot(site.coord, cif_struct.cell.cell_basis_vectors)
            atom = [site.label, site.atom_symbols[0], ionradii_dict[site.label], cart_coord, site.coord]
            atoms.append(atom)
    atmnet.atoms = atoms
    atmnet.atoms_num = len(atoms)
    return atmnet

if __name__ == "__main__":
    symm_number, symm_sybol = get_spacegroups_number_sybol(
        r"C:\Users\33389\Desktop\materials\LiScGeO4file\LiScGeO4.cif"
    )
    print(symm_number, symm_sybol)
