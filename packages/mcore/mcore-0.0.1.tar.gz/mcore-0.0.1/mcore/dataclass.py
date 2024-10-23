import json
import re
from dataclasses import dataclass, field
from typing import Union


@dataclass(frozen=True)
class Point:
    x: int = field(metadata={'check': lambda x: x >= 0})
    y: int = field(metadata={'check': lambda y: y >= 0})

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError("Coordinates must be non-negative.")

    def is_in_rect(self, rect: 'Rect') -> bool:
        return rect.x <= self.x <= rect.x + rect.w and rect.y <= self.y <= rect.y + rect.h

    def offset(self, dx: int = 0, dy: int = 0) -> 'Point':
        return Point(self.x + dx, self.y + dy)


@dataclass(frozen=True)
class Rect:
    x: int
    y: int
    w: int
    h: int

    @classmethod
    def from_dict(cls, d: dict) -> 'Rect':
        """
        从字典对象创建Rect实例。

        此方法接收一个字典，该字典应包含创建Rect实例所需的所有必要信息（'x', 'y', 'w', 'h'）。
        如果字典中缺少任何必要键或值的类型不正确，则抛出ValueError。

        参数:
        - d (dict): 包含Rect实例信息的字典。

        返回:
        - Rect: 返回一个根据字典信息创建的Rect实例。

        抛出:
        - ValueError: 如果输入字典缺少必要的键或值的类型不正确。
        """
        try:
            # 验证字典是否包含所有必要键
            if not all(key in d for key in ['x', 'y', 'w', 'h']):
                raise ValueError("Input dictionary is missing required keys: 'x', 'y', 'w', 'h'")

            # 验证字典值的类型
            if not all(isinstance(d[key], (int, float)) for key in ['x', 'y', 'w', 'h']):
                raise TypeError("All values in the input dictionary must be integers or floats")

            # 使用验证过的字典值创建Rect实例
            return cls(d['x'], d['y'], d['w'], d['h'])
        except (KeyError, ValueError, TypeError) as e:
            # 提供有意义的错误信息
            raise ValueError(f"Invalid input dictionary: {e}")

    def to_dict(self) -> dict:
        # 使用字典推导式生成返回的字典
        return {key: getattr(self, key) for key in ['x', 'y', 'w', 'h']}

    @classmethod
    def from_sequence(cls, t: Union[list[int, int, int, int], tuple[int, int, int, int]]) -> 'Rect':
        """
        从列表或元组创建一个新的 Rect 对象。

        参数:
            t (list[int] | tuple[int]): 包含四个整数的列表或元组，分别表示 x, y, w, h。

        返回:
            Rect: 新创建的 Rect 对象。

        异常:
            TypeError: 如果传入的参数不是列表或元组，或者元素不是整数。
            ValueError: 如果传入的参数数量不等于4。
        """
        if not isinstance(t, (list, tuple)):
            raise TypeError("参数必须是列表或元组")
        if len(t) != 4:
            raise ValueError("参数数量必须为4")
        if not all(isinstance(i, int) for i in t):
            raise TypeError("所有元素必须是整数")

        return cls(*t)

    def to_sequence(self) -> tuple[int, int, int, int]:
        """
        将 Rect 对象转换为元组。

        返回:
            tuple: 包含 x, y, w, h 的元组。
        """
        return self.x, self.y, self.w, self.h

    @classmethod
    def from_json(cls, j: str) -> 'Rect':
        """
        从JSON字符串创建Rect对象。

        参数:
        j (str): 表示Rect对象的JSON字符串。

        返回:
        Rect: 解析JSON字符串后创建的Rect对象。

        此方法将一个JSON字符串解析为一个Rect对象。它首先尝试将字符串解析为JSON格式，
        然后验证解析后的数据是否包含创建Rect对象所需的所有关键字段。如果解析过程中
        出现任何错误或数据格式不正确，将抛出一个ValueError。
        """
        try:
            # 将JSON字符串解析为字典
            data = json.loads(j)
            # 验证数据是否符合预期格式
            if not isinstance(data,
                              dict) or 'x' not in data or 'y' not in data or 'w' not in data or 'h' not in data:
                raise ValueError("Invalid JSON format")
            # 调用from_dict方法将验证后的数据转换为Rect对象
            return cls.from_dict(data)
        except json.JSONDecodeError as e:
            # 处理解析JSON时的错误
            raise ValueError(f"Invalid JSON: {e}")
        except Exception as e:
            # 处理其他意外错误
            raise ValueError(f"Unexpected error: {e}")

    def to_json(self) -> str:
        """
        将对象转换为JSON格式。

        该函数首先调用 `to_dict()` 方法将对象转换为字典格式，
        然后使用 `json.dumps()` 函数将字典转换为JSON格式的字符串。

        异常：
            ValueError: 如果对象无法转换为JSON格式，将抛出一个带有描述性错误信息的 ValueError。

        返回：
            str: 对象的JSON格式字符串表示。
        """
        try:
            return json.dumps(self.to_dict())
        except TypeError as e:
            raise ValueError(f"Error converting to JSON: {e}")

    def __contains__(self, item: 'Rect'):
        if not isinstance(item, Rect):
            raise TypeError("只能与 Rect 实例相减")
        return item.x >= self.x and item.y >= self.y and item.x + item.w <= self.x + self.w and item.y + item.h <= self.y + self.h

    # def __sub__(self, item: 'Rect') -> list['Rect']:
    #     """
    #     TODO:计算两个矩形差集
    #     """
    #     pass
    #
    # def __add__(self, item: 'Rect') -> list['Rect']:
    #     """
    #     TODO:计算两个矩形的并集
    #     """
    #     pass

    def size(self) -> 'Size':
        return Size(self.w, self.h)

    def center(self) -> Point:
        return Point(self.x + self.w // 2, self.y + self.h // 2)

    def left_top(self) -> Point:
        return Point(self.x, self.y)

    def right_top(self) -> Point:
        return Point(self.x + self.w, self.y)

    def right_bottom(self) -> Point:
        return Point(self.x + self.w, self.y + self.h)

    def left_bottom(self) -> Point:
        return Point(self.x, self.y + self.h)


@dataclass(frozen=True)
class RGB:
    r: int
    g: int
    b: int

    @classmethod
    def from_dict(cls, d: dict) -> 'RGB':
        """
        从字典对象创建RGB实例。
        """
        return cls(d['r'], d['g'], d['b'])

    def to_dict(self) -> dict:
        """
        将RGB实例转换为字典。
        """
        return {'r': self.r, 'g': self.g, 'b': self.b}

    @classmethod
    def from_sequence(cls, t: Union[list[int, int, int], tuple[int, int, int]]) -> 'RGB':
        """
        从列表或元组创建RGB实例。
        """
        return cls(*t)

    def to_sequence(self) -> tuple[int, int, int]:
        """
        将RGB实例转换为元组。
        """
        return self.r, self.g, self.b

    @classmethod
    def from_json(cls, j: str) -> 'RGB':
        """
        从JSON字符串创建RGB实例。
        """
        return cls.from_dict(json.loads(j))

    def to_json(self) -> str:
        """
        将RGB实例转换为JSON字符串。
        """
        return json.dumps(self.to_dict())

    def is_similar(self, other: 'RGB', threshold: int = 4):
        """
        判断两个RGB实例是否相似。
        """
        if not isinstance(other, RGB):
            raise TypeError("只能与 RGB 实例比较")
        return all(abs(a - b) <= threshold for a, b in zip(self.to_sequence(), other.to_sequence()))

    def __eq__(self, other):
        return isinstance(other, RGB) and self.r == other.r and self.g == other.g and self.b == other.b

    def __hex__(self) -> str:
        """
        将RGB对象转换成Hex字符串
        :return: Hex字符串"#ff9100"
        """
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    @classmethod
    def from_hex(cls, hex_str: str) -> 'RGB':
        """
        将Hex字符串转换成RGB对象
        :param hex_str: Hex字符串"#ff9100"
        :return: RGB对象
        """
        if hex_str[0] == "#":
            hex_str = hex_str[1:]
        # 正则表达式匹配带或不带#号的16进制颜色值
        pattern = r'^#?[A-Fa-f0-9]{6}$'
        if bool(re.match(pattern, hex_str)):
            r = int(hex_str[0:2], 16)
            g = int(hex_str[2:4], 16)
            b = int(hex_str[4:6], 16)
            return cls(r, g, b)
        else:
            raise ValueError("Invalid color format")

    def to_hex(self) -> str:
        return self.__hex__()

    def __int__(self):
        return self.r << 16 | self.g << 8 | self.b

    @classmethod
    def from_int(cls, color: int):
        """
        将颜色值转换为RGB对象
        :param color: 颜色值
        :return: RGB对象
        """
        try:
            # 验证输入是否为合法的整数
            if not isinstance(color, int) or not (0 <= color <= 0xFFFFFF):
                raise ValueError("Invalid color value. It should be an integer between 0 and 16777215.")

            # 提取红色分量
            r = (color >> 16) & 0xFF
            # 提取绿色分量
            g = (color >> 8) & 0xFF
            # 提取蓝色分量
            b = color & 0xFF

            # 返回RGB对象
            return cls(r, g, b)
        except TypeError as e:
            # 处理类型错误
            raise ValueError(f"Invalid input type. Expected an integer, got {type(color).__name__}.") from e

    def to_int(self) -> int:
        return int(self)


@dataclass(frozen=True)
class Size:
    width: int = field(metadata={'check': lambda width: width >= 0})
    height: int = field(metadata={'check': lambda height: height >= 0})

    def __post_init__(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("Width and height must be non-negative.")

    def area(self) -> int:
        """计算面积"""
        return self.width * self.height

    @classmethod
    def form_dict(cls, d: dict) -> 'Size':
        if not isinstance(d, dict) or 'width' not in d or 'height' not in d:
            raise ValueError("Input dictionary must contain 'width' and 'height' keys")
        return cls(d['width'], d['height'])

    def _as_dict(self) -> dict:
        """返回 Size 的字典表示。"""
        return {'width': self.width, 'height': self.height}

    def to_dict(self) -> dict:
        """将 Size 转换为字典。"""
        return self._as_dict()

    @classmethod
    def from_json(cls, j: str) -> 'Size':
        """从 JSON 字符串创建 Size 对象。"""
        try:
            d = json.loads(j)
            return cls.form_dict(d)
        except (json.JSONDecodeError, ValueError) as e:
            raise ValueError(f"Invalid JSON input: {e}")

    def to_json(self) -> str:
        """将 Size 对象转换为 JSON 字符串。"""
        return json.dumps(self._as_dict())

    @classmethod
    def form_sequence(cls, t: Union[list[int], tuple[int, int]]) -> 'Size':
        if not isinstance(t, (list, tuple)) or len(t) != 2 or not all(isinstance(x, int) for x in t):
            raise ValueError("Input sequence must be a list or tuple of two integers")
        return cls(*t)

    def to_sequence(self) -> tuple[int, int]:
        """将 Size 转换为元组。"""
        return self.width, self.height

    def __eq__(self, other):
        return isinstance(other, Size) and self.width == other.width and self.height == other.height
