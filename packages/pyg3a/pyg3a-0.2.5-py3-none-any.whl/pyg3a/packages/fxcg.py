#!/usr/bin/env python3


class color(int):
    import fxcg.display

    c = "color_t"


class display_fill(tuple[int, int, int, int, int]):
    import fxcg.display

    c = "display_fill"


class MBString(str):
    c = "String"


class TextColor(Enum):
    BLACK = "TEXT_COLOR_BLACK"
    BLUE = "TEXT_COLOR_BLUE"
    GREEN = "TEXT_COLOR_GREEN"
    CYAN = "TEXT_COLOR_CYAN"
    RED = "TEXT_COLOR_RED"
    PURPLE = "TEXT_COLOR_PURPLE"
    YELLOW = "TEXT_COLOR_YELLOW"
    WHITE = "TEXT_COLOR_WHITE"


class TextMode(Enum):
    NORMAL = "TEXT_MODE_NORMAL"
    INVERT = "TEXT_MODE_INVERT"
    TRANSPARENT_BACKGROUND = "TEXT_MODE_TRANSPARENT_BACKGROUND"
    AND = "TEXT_MODE_AND"


class PrintCharset(Enum):
    DEFAULT = "PRINT_CHARSET_DEFAULT"
    GB18030 = "PRINT_CHARSET_GB18030"


class DeviceType(Enum):
    CG20 = "DT_CG20"
    CG50 = "DT_CG50"
    WinSim = "DT_Winsim"


class FileCreateMode(Enum):
    FILE = "CREATEMODE_FILE"
    FOLDER = "CREATEMODE_FOLDER"


class FileOpenMode(Enum):
    READ = "READ"
    READ_SHARE = "READ_SHARE"
    WRITE = "WRITE"
    READWRITE = "READWRITE"
    READWRITE_SHARE = "READWRITE_SHARE"


class PrintMiniMode(Enum):
    TRANSPARENT_BACKGROUND = "0x02"
    INVERT = "0x04"
    STATUS_AREA = "0x40"


DEFINES: Final[dict[str, type[Types.type] | str]] = {
    # <fxcg/keyboard.h>
    "KEY_CHAR_0": int,
    "KEY_CHAR_1": int,
    "KEY_CHAR_2": int,
    "KEY_CHAR_3": int,
    "KEY_CHAR_4": int,
    "KEY_CHAR_5": int,
    "KEY_CHAR_6": int,
    "KEY_CHAR_7": int,
    "KEY_CHAR_8": int,
    "KEY_CHAR_9": int,
    "KEY_CHAR_DP": int,
    "KEY_CHAR_EXP": int,
    "KEY_CHAR_PMINUS": int,
    "KEY_CHAR_PLUS": int,
    "KEY_CHAR_MINUS": int,
    "KEY_CHAR_MULT": int,
    "KEY_CHAR_DIV": int,
    "KEY_CHAR_FRAC": int,
    "KEY_CHAR_LPAR": int,
    "KEY_CHAR_RPAR": int,
    "KEY_CHAR_COMMA": int,
    "KEY_CHAR_STORE": int,
    "KEY_CHAR_LOG": int,
    "KEY_CHAR_LN": int,
    "KEY_CHAR_SIN": int,
    "KEY_CHAR_COS": int,
    "KEY_CHAR_TAN": int,
    "KEY_CHAR_SQUARE": int,
    "KEY_CHAR_POW": int,
    "KEY_CHAR_IMGNRY": int,
    "KEY_CHAR_LIST": int,
    "KEY_CHAR_MAT": int,
    "KEY_CHAR_EQUAL": int,
    "KEY_CHAR_PI": int,
    "KEY_CHAR_ANS": int,
    "KEY_CHAR_LBRCKT": int,
    "KEY_CHAR_RBRCKT": int,
    "KEY_CHAR_LBRACE": int,
    "KEY_CHAR_RBRACE": int,
    "KEY_CHAR_CR": int,
    "KEY_CHAR_CUBEROOT": int,
    "KEY_CHAR_RECIP": int,
    "KEY_CHAR_ANGLE": int,
    "KEY_CHAR_EXPN10": int,
    "KEY_CHAR_EXPN": int,
    "KEY_CHAR_ASIN": int,
    "KEY_CHAR_ACOS": int,
    "KEY_CHAR_ATAN": int,
    "KEY_CHAR_ROOT": int,
    "KEY_CHAR_POWROOT": int,
    "KEY_CHAR_SPACE": int,
    "KEY_CHAR_DQUATE": int,
    "KEY_CHAR_VALR": int,
    "KEY_CHAR_THETA": int,
    "KEY_CHAR_A": int,
    "KEY_CHAR_B": int,
    "KEY_CHAR_C": int,
    "KEY_CHAR_D": int,
    "KEY_CHAR_E": int,
    "KEY_CHAR_F": int,
    "KEY_CHAR_G": int,
    "KEY_CHAR_H": int,
    "KEY_CHAR_I": int,
    "KEY_CHAR_J": int,
    "KEY_CHAR_K": int,
    "KEY_CHAR_L": int,
    "KEY_CHAR_M": int,
    "KEY_CHAR_N": int,
    "KEY_CHAR_O": int,
    "KEY_CHAR_P": int,
    "KEY_CHAR_Q": int,
    "KEY_CHAR_R": int,
    "KEY_CHAR_S": int,
    "KEY_CHAR_T": int,
    "KEY_CHAR_U": int,
    "KEY_CHAR_V": int,
    "KEY_CHAR_W": int,
    "KEY_CHAR_X": int,
    "KEY_CHAR_Y": int,
    "KEY_CHAR_Z": int,
    "KEY_CHAR_LOWER_A": int,
    "KEY_CHAR_LOWER_B": int,
    "KEY_CHAR_LOWER_C": int,
    "KEY_CHAR_LOWER_D": int,
    "KEY_CHAR_LOWER_E": int,
    "KEY_CHAR_LOWER_F": int,
    "KEY_CHAR_LOWER_G": int,
    "KEY_CHAR_LOWER_H": int,
    "KEY_CHAR_LOWER_I": int,
    "KEY_CHAR_LOWER_J": int,
    "KEY_CHAR_LOWER_K": int,
    "KEY_CHAR_LOWER_L": int,
    "KEY_CHAR_LOWER_M": int,
    "KEY_CHAR_LOWER_N": int,
    "KEY_CHAR_LOWER_O": int,
    "KEY_CHAR_LOWER_P": int,
    "KEY_CHAR_LOWER_Q": int,
    "KEY_CHAR_LOWER_R": int,
    "KEY_CHAR_LOWER_S": int,
    "KEY_CHAR_LOWER_T": int,
    "KEY_CHAR_LOWER_U": int,
    "KEY_CHAR_LOWER_V": int,
    "KEY_CHAR_LOWER_W": int,
    "KEY_CHAR_LOWER_X": int,
    "KEY_CHAR_LOWER_Y": int,
    "KEY_CHAR_LOWER_Z": int,
    "KEY_CTRL_NOP": int,
    "KEY_CTRL_EXE": int,
    "KEY_CTRL_DEL": int,
    "KEY_CTRL_AC": int,
    "KEY_CTRL_FD": int,
    "KEY_CTRL_UNDO": int,
    "KEY_CTRL_XTT": int,
    "KEY_CTRL_EXIT": int,
    "KEY_CTRL_SHIFT": int,
    "KEY_CTRL_ALPHA": int,
    "KEY_CTRL_OPTN": int,
    "KEY_CTRL_VARS": int,
    "KEY_CTRL_UP": int,
    "KEY_CTRL_DOWN": int,
    "KEY_CTRL_LEFT": int,
    "KEY_CTRL_RIGHT": int,
    "KEY_CTRL_F1": int,
    "KEY_CTRL_F2": int,
    "KEY_CTRL_F3": int,
    "KEY_CTRL_F4": int,
    "KEY_CTRL_F5": int,
    "KEY_CTRL_F6": int,
    "KEY_CTRL_CATALOG": int,
    "KEY_CTRL_FORMAT": int,
    "KEY_CTRL_CAPTURE": int,
    "KEY_CTRL_CLIP": int,
    "KEY_CTRL_PASTE": int,
    "KEY_CTRL_INS": int,
    "KEY_CTRL_MIXEDFRAC": int,
    "KEY_CTRL_FRACCNVRT": int,
    "KEY_CTRL_QUIT": int,
    "KEY_CTRL_PRGM": int,
    "KEY_CTRL_SETUP": int,
    "KEY_CTRL_PAGEUP": int,
    "KEY_CTRL_PAGEDOWN": int,
    "KEY_CTRL_MENU": int,
    "KEY_SHIFT_OPTN": int,
    "KEY_CTRL_RESERVE1": int,
    "KEY_CTRL_RESERVE2": int,
    "KEY_SHIFT_LEFT": int,
    "KEY_SHIFT_RIGHT": int,
    "KEY_ALPHA_MINUS": int,
    "KEY_CLIP_UP": int,
    "KEY_CLIP_DOWN": int,
    "KEY_CLIP_LEFT": int,
    "KEY_CLIP_RIGHT": int,
    "KEY_PRGM_ACON": int,
    "KEY_PRGM_DOWN": int,
    "KEY_PRGM_EXIT": int,
    "KEY_PRGM_F1": int,
    "KEY_PRGM_F2": int,
    "KEY_PRGM_F3": int,
    "KEY_PRGM_F4": int,
    "KEY_PRGM_F5": int,
    "KEY_PRGM_F6": int,
    "KEY_PRGM_LEFT": int,
    "KEY_PRGM_NONE": int,
    "KEY_PRGM_RETURN": int,
    "KEY_PRGM_RIGHT": int,
    "KEY_PRGM_UP": int,
    "KEY_PRGM_0": int,
    "KEY_PRGM_1": int,
    "KEY_PRGM_2": int,
    "KEY_PRGM_3": int,
    "KEY_PRGM_4": int,
    "KEY_PRGM_5": int,
    "KEY_PRGM_6": int,
    "KEY_PRGM_7": int,
    "KEY_PRGM_8": int,
    "KEY_PRGM_9": int,
    "KEY_PRGM_A": int,
    "KEY_PRGM_F": int,
    "KEY_PRGM_ALPHA": int,
    "KEY_PRGM_SHIFT": int,
    "KEY_PRGM_OPTN": int,
    "KEY_PRGM_MENU": int,
    "KEYWAIT_HALTON_TIMEROFF": int,
    "KEYWAIT_HALTOFF_TIMEROFF": int,
    "KEYWAIT_HALTON_TIMERON": int,
    "KEYREP_NOEVENT": int,
    "KEYREP_KEYEVENT": int,
    "KEYREP_TIMEREVENT": int,
    # <fxcg/display.h>
    "LCD_WIDTH_PX": int,
    "LCD_HEIGHT_PX": int,
    "DSA_CLEAR": int,
    "DSA_SETDEFAULT": int,
    "SAF_BATTERY": int,
    "SAF_ALPHA_SHIFT": int,
    "SAF_SETUP_INPUT_OUTPUT": int,
    "SAF_SETUP_FRAC_RESULT": int,
    "SAF_SETUP_ANGLE": int,
    "SAF_SETUP_COMPLEX_MODE": int,
    "SAF_SETUP_DISPLAY": int,
    "SAF_TEXT": int,
    "SAF_GLYPH": int,
    "COLOR_ALICEBLUE": color,
    "COLOR_ANTIQUEWHITE": color,
    "COLOR_AQUA": color,
    "COLOR_AQUAMARINE": color,
    "COLOR_AZURE": color,
    "COLOR_BEIGE": color,
    "COLOR_BISQUE": color,
    "COLOR_BLACK": color,
    "COLOR_BLANCHEDALMOND": color,
    "COLOR_BLUE": color,
    "COLOR_BLUEVIOLET": color,
    "COLOR_BROWN": color,
    "COLOR_BURLYWOOD": color,
    "COLOR_CADETBLUE": color,
    "COLOR_CHARTREUSE": color,
    "COLOR_CHOCOLATE": color,
    "COLOR_CORAL": color,
    "COLOR_CORNFLOWERBLUE": color,
    "COLOR_CORNSILK": color,
    "COLOR_CRIMSON": color,
    "COLOR_CYAN": color,
    "COLOR_DARKBLUE": color,
    "COLOR_DARKCYAN": color,
    "COLOR_DARKGOLDENROD": color,
    "COLOR_DARKGRAY": color,
    "COLOR_DARKGREEN": color,
    "COLOR_DARKKHAKI": color,
    "COLOR_DARKMAGENTA": color,
    "COLOR_DARKOLIVEGREEN": color,
    "COLOR_DARKORANGE": color,
    "COLOR_DARKORCHID": color,
    "COLOR_DARKRED": color,
    "COLOR_DARKSALMON": color,
    "COLOR_DARKSEAGREEN": color,
    "COLOR_DARKSLATEBLUE": color,
    "COLOR_DARKSLATEGRAY": color,
    "COLOR_DARKTURQUOISE": color,
    "COLOR_DARKVIOLET": color,
    "COLOR_DEEPPINK": color,
    "COLOR_DEEPSKYBLUE": color,
    "COLOR_DIMGRAY": color,
    "COLOR_DODGERBLUE": color,
    "COLOR_FIREBRICK": color,
    "COLOR_FLORALWHITE": color,
    "COLOR_FORESTGREEN": color,
    "COLOR_FUCHSIA": color,
    "COLOR_GAINSBORO": color,
    "COLOR_GHOSTWHITE": color,
    "COLOR_GOLD": color,
    "COLOR_GOLDENROD": color,
    "COLOR_GRAY": color,
    "COLOR_GREEN": color,
    "COLOR_GREENYELLOW": color,
    "COLOR_HONEYDEW": color,
    "COLOR_HOTPINK": color,
    "COLOR_INDIANRED": color,
    "COLOR_INDIGO": color,
    "COLOR_IVORY": color,
    "COLOR_KHAKI": color,
    "COLOR_LAVENDER": color,
    "COLOR_LAVENDERBLUSH": color,
    "COLOR_LAWNGREEN": color,
    "COLOR_LEMONCHIFFON": color,
    "COLOR_LIGHTBLUE": color,
    "COLOR_LIGHTCORAL": color,
    "COLOR_LIGHTCYAN": color,
    "COLOR_LIGHTGOLDENRODYELLOW": color,
    "COLOR_LIGHTGRAY": color,
    "COLOR_LIGHTGREEN": color,
    "COLOR_LIGHTPINK": color,
    "COLOR_LIGHTSALMON": color,
    "COLOR_LIGHTSEAGREEN": color,
    "COLOR_LIGHTSKYBLUE": color,
    "COLOR_LIGHTSLATEGRAY": color,
    "COLOR_LIGHTSTEELBLUE": color,
    "COLOR_LIGHTYELLOW": color,
    "COLOR_LIME": color,
    "COLOR_LIMEGREEN": color,
    "COLOR_LINEN": color,
    "COLOR_MAGENTA": color,
    "COLOR_MAROON": color,
    "COLOR_MEDIUMAQUAMARINE": color,
    "COLOR_MEDIUMBLUE": color,
    "COLOR_MEDIUMORCHID": color,
    "COLOR_MEDIUMPURPLE": color,
    "COLOR_MEDIUMSEAGREEN": color,
    "COLOR_MEDIUMSLATEBLUE": color,
    "COLOR_MEDIUMSPRINGGREEN": color,
    "COLOR_MEDIUMTURQUOISE": color,
    "COLOR_MEDIUMVIOLETRED": color,
    "COLOR_MIDNIGHTBLUE": color,
    "COLOR_MINTCREAM": color,
    "COLOR_MISTYROSE": color,
    "COLOR_MOCCASIN": color,
    "COLOR_NAVAJOWHITE": color,
    "COLOR_NAVY": color,
    "COLOR_OLDLACE": color,
    "COLOR_OLIVE": color,
    "COLOR_OLIVEDRAB": color,
    "COLOR_ORANGE": color,
    "COLOR_ORANGERED": color,
    "COLOR_ORCHID": color,
    "COLOR_PALEGOLDENROD": color,
    "COLOR_PALEGREEN": color,
    "COLOR_PALETURQUOISE": color,
    "COLOR_PALEVIOLETRED": color,
    "COLOR_PAPAYAWHIP": color,
    "COLOR_PEACHPUFF": color,
    "COLOR_PERU": color,
    "COLOR_PINK": color,
    "COLOR_PLUM": color,
    "COLOR_POWDERBLUE": color,
    "COLOR_PURPLE": color,
    "COLOR_RED": color,
    "COLOR_ROSYBROWN": color,
    "COLOR_ROYALBLUE": color,
    "COLOR_SADDLEBROWN": color,
    "COLOR_SALMON": color,
    "COLOR_SANDYBROWN": color,
    "COLOR_SEAGREEN": color,
    "COLOR_SEASHELL": color,
    "COLOR_SIENNA": color,
    "COLOR_SILVER": color,
    "COLOR_SKYBLUE": color,
    "COLOR_SLATEBLUE": color,
    "COLOR_SLATEGRAY": color,
    "COLOR_SNOW": color,
    "COLOR_SPRINGGREEN": color,
    "COLOR_STEELBLUE": color,
    "COLOR_TAN": color,
    "COLOR_TEAL": color,
    "COLOR_THISTLE": color,
    "COLOR_TOMATO": color,
    "COLOR_TURQUOISE": color,
    "COLOR_VIOLET": color,
    "COLOR_WHEAT": color,
    "COLOR_WHITE": color,
    "COLOR_WHITESMOKE": color,
    "COLOR_YELLOW": color,
    "COLOR_YELLOWGREEN": color,
    # <fxcg/registers.h>
    "P00CR": int,
    "P00DR": int,
    "P01CR": int,
    "P01DR": int,
    "P02CR": int,
    "P02DR": int,
    "P03CR": int,
    "P03DR": int,
    "P04CR": int,
    "P04DR": int,
    "P05CR": int,
    "P05DR": int,
    "P06CR": int,
    "P06DR": int,
    "P07CR": int,
    "P07DR": int,
    "P08CR": int,
    "P08DR": int,
    "P09CR": int,
    "P09DR": int,
    "P0ACR": int,
    "P0ADR": int,
    "P0BCR": int,
    "P0BDR": int,
    "P0CCR": int,
    "P0CDR": int,
    "P0DCR": int,
    "P0DDR": int,
    "P0ECR": int,
    "P0EDR": int,
    "P0FCR": int,
    "P0FDR": int,
    "P10CR": int,
    "P10DR": int,
    "P11CR": int,
    "P11DR": int,
    "P12CR": int,
    "P12DR": int,
    "P13CR": int,
    "P13DR": int,
    "P14CR": int,
    "P14DR": int,
    "P15CR": int,
    "P15DR": int,
    "P16CR": int,
    "P16DR": int,
    "P17CR": int,
    "P17DR": int,
    "P18CR": int,
    "P18DR": int,
    "P19CR": int,
    "P19DR": int,
    "P1ACR": int,
    "P1ADR": int,
    "P1BCR": int,
    "P1BDR": int,
    "P1CCR": int,
    "P1CDR": int,
    "P1DCR": int,
    "P1DDR": int,
    "P1ECR": int,
    "P1EDR": int,
    "P1FCR": int,
    "P1FDR": int,
    "P7305_SERIAL_DIRECT_PORTCR": int,
    "P7305_SERIAL_DIRECT_PORTDR": int,
    "P7305_SERIAL_TXD_BIT": int,
    "P7305_SERIAL_RXD_BIT": int,
    "P7305_ALT_SERIAL_DIRECT_PORTCR": int,
    "P7305_ALT_SERIAL_DIRECT_PORTDR": int,
    "P7305_ALT_SERIAL_RXD_BIT": int,
    "P7305_ALT_SERIAL_TXD_BIT": int,
    "P11DR_ENABLE_SERIAL": int,
    "P11CR_ENABLE_SERIAL": int,
    "P11CR_ENABLE_SERIAL_MASK": int,
    "HIZCRE": int,
    "HIZE0": int,
    "MSTPCR0": int,
    "MSTP007": int,
    "MSTP017": int,
    "MSTP024": int,
    "P7305_EXTRA_TMU0_START": int,
    "P7305_EXTRA_TMU0_CONSTANT": int,
    "P7305_EXTRA_TMU0_COUNT": int,
    "P7305_EXTRA_TMU0_CONTROL": int,
    "P7305_EXTRA_TMU1_START": int,
    "P7305_EXTRA_TMU1_CONSTANT": int,
    "P7305_EXTRA_TMU1_COUNT": int,
    "P7305_EXTRA_TMU1_CONTROL": int,
    "P7305_EXTRA_TMU2_START": int,
    "P7305_EXTRA_TMU2_CONSTANT": int,
    "P7305_EXTRA_TMU2_COUNT": int,
    "P7305_EXTRA_TMU2_CONTROL": int,
    "P7305_EXTRA_TMU3_START": int,
    "P7305_EXTRA_TMU3_CONSTANT": int,
    "P7305_EXTRA_TMU3_COUNT": int,
    "P7305_EXTRA_TMU3_CONTROL": int,
    "P7305_EXTRA_TMU4_START": int,
    "P7305_EXTRA_TMU4_CONSTANT": int,
    "P7305_EXTRA_TMU4_COUNT": int,
    "P7305_EXTRA_TMU4_CONTROL": int,
    "P7305_EXTRA_TMU5_START": int,
    "P7305_EXTRA_TMU5_CONSTANT": int,
    "P7305_EXTRA_TMU5_COUNT": int,
    "P7305_EXTRA_TMU5_CONTROL": int,
    "RTC_port": int,
    "CBR0": int,
    "CRR0": int,
    "CAR0": int,
    "CAMR0": int,
    "CBR1": int,
    "CRR1": int,
    "CAR1": int,
    "CAMR1": int,
    "CDR1": int,
    "CDMR1": int,
    "CETR1": int,
    "CCMFR": int,
    "CBCR": int,
    # <fxcg/tmu.h>
    "REG_TMU_TSTR": "unsigned char*",
    "REG_TMU_TCOR_0": "unsigned int*",
    "REG_TMU_TCNT_0": "unsigned int*",
    "REG_TMU_TCR_0": "unsigned short*",
    "REG_TMU_TCOR_1": "unsigned int*",
    "REG_TMU_TCNT_1": "unsigned int*",
    "REG_TMU_TCR_1": "unsigned short*",
    "REG_TMU_TCOR_2": "unsigned int*",
    "REG_TMU_TCNT_2": "unsigned int*",
    "REG_TMU_TCR_2": "unsigned short*",
}


def PrintXY(x: int, y: int, message: str, mode: int = 0, color: int = 0) -> None:
    import fxcg.display

    return f'PrintXY({x}, {y}, (String("  ") + {message}).c_str(), {mode}, {color})'


def EditMBStringChar(MB_string: str, xpos: int, char_to_insert: int) -> tuple[str, int]:
    import fxcg.keyboard

    @struct_c_func
    def _EditMBStringChar(MB_string: str, xpos: int, char_to_insert: int) -> tuple[str, int]:
        return """
        String new_str = String(MB_string, MB_string.length() + 1);
        int cursor = EditMBStringChar((unsigned char*) new_str.c_str(), MB_string.length() + 1, xpos, char_to_insert);
        return {new_str, cursor};
        """

    return f"_EditMBStringChar({MB_string}, {xpos}, {char_to_insert})"


def DisplayMBString(buffer: str, start: int, cursor: int, x: int, y: int) -> None:
    import fxcg.keyboard

    return f"DisplayMBString((unsigned char*) {buffer}.c_str(), {start}, {cursor}, {x}, {y})"


def EditMBStringCtrl(
    MB_string: str, start: int, xpos: int, key: int, x: int, y: int, posmax: int = 256
) -> tuple[str, int, int, int]:
    import fxcg.keyboard

    @struct_c_func
    def _EditMBStringCtrl(
        MB_string: str, start: int, xpos: int, key: int, x: int, y: int, posmax: int
    ) -> tuple[str, int, int, int]:
        return """
        String new_str = String(MB_string, posmax);
        EditMBStringCtrl((unsigned char*) new_str.c_str(), posmax, &start, &xpos, &key, x, y);
        return {new_str, start, xpos, key};
        """

    return f"_EditMBStringCtrl({MB_string}, {start}, {xpos}, {key}, {x}, {y}, {posmax})"


def PrintMini(
    x: int,
    y: int,
    string: str,
    mode_flags: int = 0,
    xlimit: int = 0xFFFFFFFF,
    color: color = 0,
    back_color: color = 0xFFFF,
    writeflag: int = 1,
    *,
    P6: int = 0,
    P7: int = 0,
    P11: int = 0,
) -> tuple[int, int]:
    import fxcg.display

    @struct_c_func
    def _PrintMini(
        x: int,
        y: int,
        string: str,
        mode_flags: int,
        xlimit: int,
        P6: int,
        P7: int,
        color: int,
        back_color: int,
        writeflag: int,
        P11: int,
    ) -> tuple[int, int]:
        return """
        int xpos = x;
        int ypos = y;
        PrintMini(&xpos, &ypos, string.c_str(), mode_flags, (unsigned int) xlimit, P6, P7, color, back_color, writeflag, P11);
        return {xpos, ypos};
        """

    return (
        f"_PrintMini({x}, {y}, {string}, {mode_flags}, {xlimit}, {P6}, {P7}, {color}, {back_color}, {writeflag}, {P11})"
    )


def Bdisp_AreaClr(area: display_fill, target: bool, color: color = 0) -> None:
    import fxcg.display

    return f"Bdisp_AreaClr(&{area}, {target}, {color})"


def SetGetkeyToMainFunctionReturnFlag(enabled: bool) -> None:
    """
    CODE (originally) BY SIMON LOTHAR, AVAILABLE ON "fx_calculators_SuperH_based.chm" version 16
    the function assumes, that the RAM-pointer to GetkeyToMainFunctionReturnFlag is loaded
    immediately by a "Move Immediate Data"-instruction
    """

    @c_func
    def _SetGetkeyToMainFunctionReturnFlag(enabled: bool) -> None:
        return """
        int addr, addr2;

        // get the pointer to the syscall table
        addr = *(unsigned char*)0x80020071;     // get displacement

        addr++;
        addr *= 4;
        addr += 0x80020070;
        addr = *(unsigned int*)addr;

        if ( addr < (int)0x80020070 ) return;
        if ( addr >= (int)0x81000000 ) return;

        // get the pointer to syscall 1E99
        addr += 0x1E99*4;
        if ( addr < (int)0x80020070 ) return;
        if ( addr >= (int)0x81000000 ) return;

        addr = *(unsigned int*)addr;
        if ( addr < (int)0x80020070 ) return;
        if ( addr >= (int)0x81000000 ) return;

        switch ( *(unsigned char*)addr ){
                case 0xD0 : // MOV.L @( disp, PC), Rn (REJ09B0317-0400 Rev. 4.00 May 15, 2006 page 216)
                case 0xD1 :
                case 0xD2 :
                case 0xD3 :
                case 0xD4 :
                case 0xD5 :
                case 0xD6 :
                case 0xD7 :
                case 0xD8 :
                        addr2 = *(unsigned char*)( addr + 1 );  // get displacement
                        addr2++;
                        addr2 *= 4;
                        addr2 += addr;
                        addr2 &= ~3;

                        if ( addr2 < (int)0x80020070 ) return;
                        if ( addr2 >= (int)0x81000000 ) return;

                        addr = *(unsigned int*)addr2;
                        if ( ( addr & 0xFF000000 ) != 0x88000000 && ( addr & 0xFF000000 ) != 0x8C000000 ) return; // MODIFIED for CG50 or CG10/20 (memory address change)

                        // finally perform the desired operation and set the flag:
                        if ( enabled ) *(unsigned char*)addr = 0;
                        else *(unsigned char*)addr = 3;

                        break;

                default : addr = 0x100;
        }
        """

    return f"_SetGetkeyToMainFunctionReturnFlag({enabled})"


def Timer_Install(handler: Callable[[], Any], elapse: int, internal_timer_id: int = 0) -> int:
    import fxcg.system

    return f"Timer_Install({internal_timer_id}, {handler}, {elapse})"


def PowerOff(display_logo: bool = True) -> None:
    import fxcg.system

    return f"PowerOff({display_logo})"


def GetLatestUserInfo() -> tuple[str, str, str]:
    @struct_c_func
    def _GetLatestUserInfo() -> tuple[str, str, str]:
        return r"""
        // Search through user info
        char *flagpointer = (char *) 0x80BE0000;
        int counter = 0;
        while (*flagpointer == 0x0F) {
            flagpointer = flagpointer + 0x40;
            counter++;
        }

        // Set password from latest info
        if (counter) {
            flagpointer = flagpointer - 0x40;
            if(*(flagpointer + 0x2C) != '\\0') {
                return {String(flagpointer + 0x04), String(flagpointer + 0x18), String(flagpointer + 0x2C)};
            }
        }
        
        // Otherwise return blank strings
        return {String(), String(), String()};
        """

    return f"_GetLatestUserInfo()"


def GetKey(key: int = None) -> int:
    import fxcg.keyboard

    if key:
        return f"GetKey(&{key})"

    @c_func
    def _GetKey() -> int:
        return """
        int _tmp_var;
        GetKey(&_tmp_var);
        return _tmp_var;
        """

    return f"_GetKey()"


def GetKeyWait_OS(type_of_waiting: int = 0, timeout_period: int = 0, menu: int = 0) -> tuple[int, int, int]:
    import fxcg.display

    @struct_c_func
    def _GetKeyWait_OS(type_of_waiting: int, timeout_period: int, menu: int) -> tuple[int, int, int]:
        return """
        int column, row;
        unsigned short keycode;
        GetKeyWait_OS(&column, &row, type_of_waiting, timeout_period, menu, &keycode);
        return {column, row, (int) keycode};
        """

    return f"_GetKeyWait_OS({type_of_waiting}, {timeout_period}, {menu})"


def GetMainBatteryVoltage() -> int:
    import fxcg.system

    return "GetMainBatteryVoltage(1)"


def RTC_GetTicks() -> int:
    import fxcg.rtc

    return "RTC_GetTicks()"


def GetVRAMAddress() -> tuple[color, ...]:
    import fxcg.display

    return "(color_t *) GetVRAMAddress()"


def ProgressBar(msg: str, current: int, total: int) -> None:
    import fxcg.display

    return f"ProgressBar2((unsigned char *){msg}.c_str(), {current}, {total})"


def ProgressBar(current: int, total: int) -> None:
    import fxcg.display

    return f"ProgressBar({current}, {total})"


def LocalizeMessage(msgno: int) -> MBString:
    import fxcg.display

    @c_func
    def _LocalizeMessage(msgno: int) -> MBString:
        return """
        char buffer[90];
        LocalizeMessage1(msgno, buffer);
        return String(buffer);
        """

    return f"_LocalizeMessage({msgno})"


def DefineStatusMessage(msg: str, indexed_color: int, *, P2: int = 0, P4: int = 0) -> None:
    import fxcg.display

    return f"DefineStatusMessage((char *)({msg}).c_str(), {P2}, {indexed_color}, {P4})"


def MB_ElementCount(buf: MBString) -> int:
    import fxcg.system

    return f"MB_ElementCount((char *) ({buf}).c_str())"


def len(s: MBString) -> int:
    import fxcg.system

    return f"MB_ElementCount((char *) ({s}).c_str())"


def Print_OS(msg: str, mode: int = 0, *, zero2: int = 0) -> None:
    import fxcg.display

    return f"Print_OS(({msg}).c_str(), {mode}, {zero2})"


def PrintXY_2(lines: int, x: int, y: int, msgno: int, color: int = 0) -> None:
    import fxcg.display

    return f"PrintXY_2({lines}, {x}, {y}, {msgno}, {color})"
