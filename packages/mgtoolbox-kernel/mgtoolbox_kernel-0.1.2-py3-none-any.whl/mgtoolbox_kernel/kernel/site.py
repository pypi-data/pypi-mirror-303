from typing import Dict, Union, List
import math
import numpy as np
from .mgclass import MGobject
from .atom import Atom


class Site(MGobject):
    """
    Site 站点类
    用于描述材料结构中的站点
    Parameters
    ----------
    object : [type]
        [description]
    """

    def __init__(
        self,
        coord: np.ndarray,
        occupier: Dict[Atom, float] = None,
        label: str = "",
        site_type: str = "",
        attributes: Dict = None,
    ):
        """
        __init__ 站点类初始化
        站点类初始化函数
        Parameters
        ----------
        coords : np.ndarray
            站点位置分数坐标
        occupier : Dict, optional
            站点包含的原子及占据率信息, by default None
        label: str, optional
            站点标签信息
        label: str, optional
            站点类型信息
        attributes : Dict, optional
            站点类的其它可自定义属性, by default None。 如{"radius":10}
        """
        if attributes is None:
            super().__init__(attributes={})
        else:
            super().__init__(attributes)
        self.label: str = label
        self.type: str = site_type
        self.coord: np.ndarray = np.array(coord)
        if occupier is None:
            self.occupier: Dict[Atom, float] = {}
        else:
            self.occupier: Dict[Atom, float] = occupier


    def __eq__(self, other: "Site") -> bool:
        # 判断是否同一站点仅比较站点坐标
        return np.all(np.isclose(self.coord, other.coord, rtol=0.001))

    def __str__(self) -> str:
        site_string = (
            "\n{"
            + "label:"
            + self.label
            + ", type:"
            + str(self.type)
            + ", coord:"
            + str(self.coord)
            + ", occupier:"
            + str(self.occupier)
            + "}"
        )
        return site_string

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def atoms(self) -> list:
        return list(self.occupier.keys())

    @property
    def atom_symbols(self) -> list:
        return [atom.symbol for atom in self.occupier.keys()]

    @property
    def atom_valences(self) -> list:
        return [atom.valence_state for atom in self.occupier.keys()]

    @property
    def atom_occupancies(self) -> list:
        return list(self.occupier.values())

    @property
    def x(self) -> float:
        return self.coord[0]

    @property
    def y(self) -> float:
        return self.coord[1]

    @property
    def z(self) -> float:
        return self.coord[2]

    @x.setter
    def x(self, x: float):
        self.coord[0] = x

    @y.setter
    def y(self, y: float):
        self.coord[1] = y

    @z.setter
    def z(self, z: float):
        self.coord[2] = z

    @property
    def is_ordered(self):
        """站点是否有序(满足站点上只包含一个原子且占据率为1.0)

        Returns
        -------
        bool
            是否有序
        """
        return len(self.atoms) == 1 and math.isclose(self.atom_occupancies[0], 1.0)

    def get_element_occupy(self, symbol: str):
        """_summary_

        Parameters
        ----------
        symbol : str
            _description_

        Returns
        -------
        _type_
            _description_
        """        
        for atom, occupy in self.occupier.items():
            if atom.symbol == symbol:
                return occupy

    def assign_occupier(self, atom: Atom, occupy: float = 1.0):
        """
        assign_occupier 设置站点包含的原子信息

        设置站点包含的原子，如原子类型，占有率。

        Parameters
        ----------
        atom : Atom
            [添加的原子类型]
        occupy : float, optional
            [占据率], by default 1.0
        """
        if atom in self.atoms:  # 若站点上已存在该原子类型，则将占据率求和
            self.occupier[atom] += occupy
        else:
            self.occupier[atom] = occupy

    def assign_occupier_by_dict(self, occupiper_dict):
        """_summary_

        Parameters
        ----------
        occupiper_dict : _type_
            _description_
        """        
        for k, v in occupiper_dict.items():
            self.assign_occupier(k, v)

    def assign_occupier_by_symbol(
        self, symbol: str = "", valence_state: float = 0.0, occupy: float = 1.0
    ):
        """_summary_

        Parameters
        ----------
        symbol : str, optional
            _description_, by default ""
        valence_state : float, optional
            _description_, by default 0.0
        occupy : float, optional
            _description_, by default 1.0

        Raises
        ------
        ValueError
            _description_
        """        
        if len(symbol) > 0:
            atom = Atom(symbol, valence_state)
            if atom not in self.atoms:
                self.assign_occupier(atom, occupy)
        else:
            raise ValueError("Symbol cannot be empty!!!")

    def get_occupy_sum(self):
        """_summary_

        Returns
        -------
        _type_
            _description_

        Raises
        ------
        ValueError
            _description_
        """        
        occu_sum = 0
        for occupy in self.occupier.values():
            occu_sum = occu_sum + occupy
        if occu_sum > 1.0:
            raise ValueError("occupy > 1.0")
        return occu_sum

