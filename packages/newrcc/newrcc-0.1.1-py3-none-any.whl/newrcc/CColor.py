from newrcc import CError

Reset = '\033[0m'


class Color:
    def __init__(self, color: str | tuple[int, int, int]):
        if isinstance(color, str):
            self.colorcode = color
        elif isinstance(color, tuple):
            Color.__RGBColor(self, color)
        else:
            raise CError.CDColorUndefinedError(color)

    def __RGBColor(self, color: tuple[int, int, int]):
        for code in color:
            if not (0 <= code <= 255):
                raise CError.CDColorUndefinedError(color)
        if isinstance(self, TextColor):
            _type = '38'
        elif isinstance(self, BackgroundColor):
            _type = '48'
        else:
            raise CError.CDColorUndefinedError(color)
        self.colorcode = f'\033[{_type};2;{color[0]};{color[1]};{color[2]}m'

    def __str__(self):
        return self.colorcode


class TextColor(Color):
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    GRAY = '\033[37m'
    Dark_GRAY = '\033[90m'
    Light_RED = '\033[91m'
    Light_GREEN = '\033[92m'
    Light_YELLOW = '\033[93m'
    Light_BLUE = '\033[94m'
    Light_PURPLE = '\033[95m'
    Light_CRAY = '\033[96m'
    Light_GRAY = '\033[97m'

    def __init__(self, color: str | tuple[int, int, int]):
        super().__init__(color)


class BackgroundColor(Color):
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    GRAY = '\033[47m'

    def __init__(self, color: str | tuple[int, int, int]):
        super().__init__(color)


class Decoration:
    Bold = '\033[1m'
    Italic = '\033[3m'
    L_UnderLine = '\033[4m'
    ColorReverse = '\033[7m'
    MiddleLine = '\033[9m'
    B_UnderLine = '\033[21m'

    def __init__(self, decoration: str):
        self.decoration = decoration

    def __str__(self):
        return self.decoration
