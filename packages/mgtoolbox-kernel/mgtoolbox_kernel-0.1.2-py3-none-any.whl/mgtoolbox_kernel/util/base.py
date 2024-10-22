# -*- encoding: utf-8 -*-
import math
import re
import numpy as np
import periodictable as pt
from typing import Tuple

def parse_sitesym(symlist, sep=','):
    """Parses a sequence of site symmetries in the form used by
    International Tables and returns corresponding rotation and
    translation arrays.

    Example:

    >>> symlist = [
    ...     'x,y,z',
    ...     '-y+1/2,x+1/2,z',
    ...     '-y,-x,-z',
    ... ]
    >>> rot, trans = parse_sitesym(symlist)
    >>> rot
    array([[[ 1,  0,  0],
            [ 0,  1,  0],
            [ 0,  0,  1]],
    <BLANKLINE>
        [[ 0, -1,  0],
            [ 1,  0,  0],
            [ 0,  0,  1]],
    <BLANKLINE>
        [[ 0, -1,  0],
            [-1,  0,  0],
            [ 0,  0, -1]]])
    >>> trans
    array([[ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0. ],
        [ 0. ,  0. ,  0. ]])
    """
    nsym = len(symlist)
    rot = np.zeros((nsym, 3, 3), dtype='int')
    trans = np.zeros((nsym, 3))
    
    trans_pattern = r"([-+]?\d*\.\d*|[-+]?\d+)"
    re_trans = re.compile(trans_pattern)
    rot_pattern=r"[+-]?[xyz]"
    re_rot = re.compile(rot_pattern)
    
    for i, sym in enumerate(symlist):
        for j, s in enumerate(sym.split(sep)):
            s = s.lower().strip()
            #得到旋转字符
            strs_matches = re_rot.findall(s)
            #得到偏移数字
            numbers_matches = re_trans.findall(s)
            if len(numbers_matches)==2:
                trans[i, j] = float(numbers_matches[0]) / float(numbers_matches[1])
            elif len(numbers_matches)==1:
                trans[i, j] = float(numbers_matches[0])
            elif len(numbers_matches)==0:
                trans[i, j] = 0.0
            else:
                raise Exception("Read symmetry trans string  error")
            if len(strs_matches)<1:
                raise Exception(
                        'Error parsing %r. Invalid site symmetry: %s' %
                        (s, sym))
            for sxyz in strs_matches:
                sign = 1.0
                if len(sxyz)==2:
                    if sxyz[0] in '+-':
                        if sxyz[0] == '-':
                            sign = -1.0
                    xyz=sxyz[1]
                elif len(sxyz)==1:
                    xyz=sxyz[0]
                    sign = 1.0
                else:
                    raise Exception(
                        'Error parsing %r. Invalid site symmetry: %s' %
                        (s, sym))
                if xyz in 'xyz':
                    k = ord(xyz) - ord('x')
                    rot[i, j, k] = sign
    return rot, trans
def get_lattice_vectors(a, b, c, alpha, beta, gamma) -> np.ndarray:
    """Get the cell vectors matrix(fix a-axis) from the cell parameters
    Parameters
    ----------
    a : float
        晶格参数:a
    b : float
        晶格参数:b
    c : float
        晶格参数:c
    alpha : float
        晶格参数:alpha
    beta : float
        晶格参数:beta
    gamma : float
        晶格参数:gamma

    Returns
    -------
    numpy.ndarray
        晶格矢量矩阵
    """
    angles_r = np.radians([alpha, beta, gamma])
    cos_alpha, cos_beta, cos_gamma = np.cos(angles_r)
    sin_alpha, sin_beta, sin_gamma = np.sin(angles_r)

    # fix a-axis
    vector_a = a * np.array([1, 0, 0])
    vector_b = b * np.array([cos_gamma, sin_gamma, 0])
    cx = cos_beta
    cy = (cos_alpha - cos_beta * cos_gamma) / sin_gamma
    cz_sqr = 1. - cx * cx - cy * cy
    cz = np.sqrt(cz_sqr)
    vector_c = c * np.array([cx, cy, cz])
    return np.array([vector_a, vector_b, vector_c])


def get_lattice_parameters(lattice_vectors: np.ndarray) -> Tuple:
    """get lattice parameters from the lattice vectors matrix

    Parameters
    ----------
    lattice_vectors : np.ndarray
        晶格矢量

    Returns
    -------
    元组类型
        返回晶格常数:a,b,c,alpha,beta,gamma
    """
    abc = np.linalg.norm(lattice_vectors, axis=1)
    arc_alpha = np.arccos(np.dot(lattice_vectors[1], lattice_vectors[2]) / (abc[1] * abc[2]))
    arc_beta = np.arccos(np.dot(lattice_vectors[0], lattice_vectors[2]) / (abc[0] * abc[2]))
    arc_gamma = np.arccos(np.dot(lattice_vectors[1], lattice_vectors[0]) / (abc[1] * abc[0]))
    arc_values = np.array([arc_alpha, arc_beta, arc_gamma])
    alpha, beta, gamma = arc_values * 180 / math.pi
    return tuple([abc[0], abc[1], abc[2], alpha, beta, gamma])

