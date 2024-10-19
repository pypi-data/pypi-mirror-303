
# Filler class to use in type hints
class RGBValue():
    def __init__(self):
        return

class HexValue():
    def __init__(self, hexCode: str):
        self.code = hexCode.replace("#", "")

    def toRGB(self) -> RGBValue:
        rgbTuple = tuple(int(self.code[i:i+2], 16) for i in (0, 2, 4))
        return RGBValue(rgbTuple[0], rgbTuple[1], rgbTuple[2])

    def __repr__(self) -> str:
        return "#" + self.code

class RGBValue():
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b
        

    def toHex(self) -> HexValue:
        return HexValue(('{:02X}' * 3).format(self.r, self.g, self.b))

    def __repr__(self) -> str:
        return f"RGBValue({self.r}, {self.g}, {self.b})"


class ColorLogic():
    # CLEAR
    CLEAR = '\033[0m'
    RESET = CLEAR

    def __init__(self, rgb: RGBValue):
        self.rgbValue = rgb
        self.hexValue = rgb.toHex()
    
    def rgb(self) -> RGBValue:
        return self.rgbValue
    
    def hex(self) -> HexValue:
        return self.hexValue
    
    def bg(self) -> str:
        return f'\033[48;2;{self.rgbValue.r};{self.rgbValue.g};{self.rgbValue.b}m'
    
    def __repr__(self) -> str:
        return f'\033[38;2;{self.rgbValue.r};{self.rgbValue.g};{self.rgbValue.b}m'

class Color(ColorLogic):

    # GRAY SCALE
    WHITE = ColorLogic(RGBValue(255, 255, 255))
    SILVER = ColorLogic(RGBValue(192, 192, 192))
    GRAY = ColorLogic(RGBValue(128, 128, 128))
    GREY = ColorLogic(RGBValue(128, 128, 128))
    BLACK = ColorLogic(RGBValue(0, 0, 0))

    # REDS
    RED = ColorLogic(RGBValue(255, 0, 0))
    DARK_RED = ColorLogic(RGBValue(128, 0, 0))

    # YELLOWS
    YELLOW = ColorLogic(RGBValue(255, 255, 0))
    DARK_YELLOW = ColorLogic(RGBValue(128, 128, 0))

    # GREENS
    GREEN = ColorLogic(RGBValue(0, 255, 0))
    DARK_GREEN = ColorLogic(RGBValue(0, 128, 0))

    # BLUES
    AQUA = ColorLogic(RGBValue(0, 255, 255))
    LIGHT_BLUE = AQUA
    TEAL = ColorLogic(RGBValue(0, 128, 128))
    BLUE = ColorLogic(RGBValue(0, 0, 255))
    NAVY = ColorLogic(RGBValue(0, 0, 255))
    DARK_BLUE = NAVY

    # PINKS
    PINK = ColorLogic(RGBValue(255, 0, 255))

    # PURPLES
    PURPLE = ColorLogic(RGBValue(128, 0, 128))


print(f"{Color.BLUE}")