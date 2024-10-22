import math
from .mgclass import MGobject


class Atom(MGobject):
    """Atom 离子类型
    用于表示结构中离子类型
    Parameters
    ----------
    object : [type]
        [description]
    """

    def __init__(self, symbol: str, valence_state: float):
        """__init__ 初始化函数

        Parameters
        ----------
        symbol : str 离子类型
            离子类型 如O,Fe,Al3+,Li1+ 等
        valence_state : [float]
            离子化合价
        attributes: dict
            其他属性
        """
        super().__init__()
        # 离子元素类型 O，Fe etc
        self.symbol: str = symbol
        # 离子化合价  -1,+2，...等。
        self.valence_state: float = valence_state
        self.hash_value = hash(self.symbol + str(self.valence_state))

    def __eq__(self, other: 'Atom') -> bool:
        return self.symbol == other.symbol and (
            math.fabs(self.valence_state - other.valence_state) < 0.001)

    def __str__(self) -> str:
        return '[symbol_type:' + self.symbol + ', valence:' + str(
            self.valence_state) + ']'

    def __hash__(self):
        return self.hash_value

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        # 定义 < 操作符
        return self.symbol < other.symbol

    def __gt__(self, other):
        # 定义 > 操作符
        return self.symbol > other.symbol
