import re

from pydantic import BaseModel, Field


class Point(BaseModel):
    x: int = Field(..., ge=0, description="x-coordinate, must be non-negative")
    y: int = Field(..., ge=0, description="y-coordinate, must be non-negative")

    def is_in_rect(self, rect: 'Rect') -> bool:
        return rect.x <= self.x <= rect.x + rect.w and rect.y <= self.y <= rect.y + rect.h

    def offset(self, dx: int = 0, dy: int = 0) -> 'Point':
        return Point(x=self.x + dx, y=self.y + dy)


class Rect(BaseModel):
    x: int = Field(..., ge=0, description="x-coordinate, must be non-negative")
    y: int = Field(..., ge=0, description="y-coordinate, must be non-negative")
    w: int = Field(..., gt=0, description="width, must be greater than zero")
    h: int = Field(..., gt=0, description="height, must be greater than zero")

    def __contains__(self, item: 'Rect'):
        if not isinstance(item, Rect):
            raise TypeError("只能与 Rect 实例相比较")
        return item.x >= self.x and item.y >= self.y and item.x + item.w <= self.x + self.w and item.y + item.h <= self.y + self.h

    def size(self) -> 'Size':
        return Size(width=self.w, height=self.h)

    def center(self) -> 'Point':
        return Point(x=self.x + self.w // 2, y=self.y + self.h // 2)

    def left_top(self) -> 'Point':
        return Point(x=self.x, y=self.y)

    def right_top(self) -> 'Point':
        return Point(x=self.x + self.w, y=self.y)

    def right_bottom(self) -> 'Point':
        return Point(x=self.x + self.w, y=self.y + self.h)

    def left_bottom(self) -> 'Point':
        return Point(x=self.x, y=self.y + self.h)


class RGB(BaseModel):
    r: int = Field(..., ge=0, le=255, description="Red value must be between 0 and 255")
    g: int = Field(..., ge=0, le=255, description="Green value must be between 0 and 255")
    b: int = Field(..., ge=0, le=255, description="Blue value must be between 0 and 255")

    def is_similar(self, other: 'RGB', threshold: int = 4) -> bool:
        """
        判断两个RGB实例是否相似。
        """
        if not isinstance(other, RGB):
            raise TypeError("只能与 RGB 实例比较")
        return all(abs(a - b) <= threshold for a, b in zip((self.r, self.g, self.b), (other.r, other.g, other.b)))

    def __hex__(self) -> str:
        """
        将RGB对象转换成Hex字符串
        """
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    @classmethod
    def from_hex(cls, hex_str: str) -> 'RGB':
        """
        将Hex字符串转换成RGB对象
        """
        if hex_str.startswith("#"):
            hex_str = hex_str[1:]
        pattern = r'^[A-Fa-f0-9]{6}$'
        if bool(re.match(pattern, hex_str)):
            r = int(hex_str[0:2], 16)
            g = int(hex_str[2:4], 16)
            b = int(hex_str[4:6], 16)
            return cls(r=r, g=g, b=b)
        else:
            raise ValueError("Invalid color format")

    def hex(self) -> str:
        return self.__hex__()

    def __int__(self) -> int:
        return (self.r << 16) | (self.g << 8) | self.b

    @classmethod
    def from_int(cls, color: int) -> 'RGB':
        """
        将颜色值转换为RGB对象
        """
        if not (0 <= color <= 0xFFFFFF):
            raise ValueError("颜色值应该在 0 到 16777215 之间。")
        r = (color >> 16) & 0xFF
        g = (color >> 8) & 0xFF
        b = color & 0xFF
        return cls(r=r, g=g, b=b)

    def int(self) -> int:
        return int(self)


class Size(BaseModel):
    width:int = Field(..., ge=0, description="width, must be greater than zero")
    height:int = Field(..., ge=0, description="height, must be greater than zero")

    def area(self) -> int:
        """计算面积"""
        return self.width * self.height
