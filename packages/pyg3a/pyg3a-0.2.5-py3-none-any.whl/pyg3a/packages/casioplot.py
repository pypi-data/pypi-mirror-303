#!/usr/bin/env python3

import fxcg.display


def show_screen() -> None:
    return "Bdisp_PutDisp_DD()"


def clear_screen() -> None:
    @c_func
    def _clear_screen() -> None:
        return """
        unsigned int *p = (unsigned int *) GetVRAMAddress();
        for (int i = 0; i < LCD_WIDTH_PX; i++) {
            for (int j = 0; j < LCD_HEIGHT_PX; j++) *p++ = 0;
        }
        """

    return "_clear_screen()"


def set_pixel(x: int, y: int, color: [int, int, int]) -> None:
    return f"Bdisp_SetPoint_VRAM({x}, {y}, (({color[0]} & 248) << 8) | (({color[1]} & 252) << 3) | ({color[2]} >> 3))"


def get_pixel(x: int, y: int) -> tuple[int, int, int]:
    @struct_c_func
    def _get_pixel(x: int, y: int) -> tuple[int, int, int]:
        return """
        unsigned short color = Bdisp_GetPoint_VRAM(x, y);
        return {((colour >> 11) & 0x1F) << 1, (colour >> 5) & 0x2F, colour & 0x1F};
        """

    return f"_get_pixel({x}, {y})"


def draw_string(x: int, y: int, text: str, color: [int, int, int], size: str) -> None:
    @syscall(0x23F)
    def PrintMiniMini2(
        x: "int *",
        y: "int *",
        message: "const char *",
        mode: int,
        xlimit: "unsigned int",
        P6: int,
        P7: int,
        color: "color",
        back_color: "color",
        writeflag: int,
        P11: int,
    ) -> None: ...

    @c_func
    def _draw_string(x: int, y: int, text: str, color: "color", size: str) -> None:
        return """
        if (size == String("large"))
            PrintCXY(x, y, text.c_str(), TEXT_MODE_NORMAL, -1, color, COLOR_WHITE, 1, 0);
        else if (size == String("medium"))
            PrintMini(&x, &y, text.c_str(), TEXT_MODE_NORMAL, -1, 0, 0,  color, COLOR_WHITE, 1, 0);
        else
            PrintMiniMini2(&x, &y, text.c_str(), TEXT_MODE_NORMAL, -1, 0, 0, color, COLOR_WHITE, 1, 0);
        """

    return f"_draw_string({x}, {y}, {text}, (({color[0]} & 248) << 8) | (({color[1]} & 252) << 3) | ({color[2]} >> 3), {size})"
