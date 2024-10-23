from enum import Enum

RESET = '\033[0m' # called to return to standard terminal text color
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

class Foreground(Enum):
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m' # orange on some systems
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'

class Background(Enum):
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m' # orange on some systems
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    LIGHT_GRAY = '\033[47m'
    DARK_GRAY = '\033[100m'
    BRIGHT_RED = '\033[101m'
    BRIGHT_GREEN = '\033[102m'
    BRIGHT_YELLOW = '\033[103m'
    BRIGHT_BLUE = '\033[104m'
    BRIGHT_MAGENTA = '\033[105m'
    BRIGHT_CYAN = '\033[106m'
    WHITE = '\033[107m'

def print_c(text:str, foreground:Foreground = None, background:Background = None, bold:bool = False, underline:bool = False):
    lines = text.split('\n')
    for line in lines:
        
        out_str = ''
        
        parts = line.split('\t')
        for part in parts:
            out_str += part
            while len(out_str) % 5 != 0:
                out_str += ' '

        if bold:
            out_str = BOLD + out_str
        if underline:
            out_str = UNDERLINE + out_str
        if foreground is not None:
            out_str = foreground.value + out_str
        if background is not None:
            out_str = background.value + out_str
        out_str += RESET
        print(out_str)

def warn(text:str):
    print_c(f'WARNING:\t{text}', foreground=Foreground.YELLOW)

def error(text:str):
    print_c(f'ERROR:\t{text}', foreground=Foreground.RED)

def success(text:str):
    print_c(f'SUCCESS:\t{text}', foreground=Foreground.BRIGHT_GREEN)

if __name__ == '__main__':
    print_c('DEFAULT', foreground=Foreground.RED, background=Background.YELLOW)

    for foreground in Foreground:
        for background in Background:
            print_c(f'{foreground.name} on {background.name}', foreground, background)

    print_c('Test1.1\tTest1.2\nTest20.1\tTest2.2', foreground=Foreground.RED)

    print_c('BOLD', bold=True)
    print_c('UNDERLINE', underline=True)

    warn('This is a warning.')
    error('This is an error.')
    success('This operation succeeded.')