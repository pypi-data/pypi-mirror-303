from typing import Tuple

def hex2rgb(hex_code: str) -> Tuple[int, int, int]:
    """Converts a given hex string to RGB color code format."""
    
    if hex_code.startswith("#"):
        hex_code = hex_code[1:]

    if not (len(hex_code) == 3 or len(hex_code) == 6):
        raise ValueError("Hex code length should be either 3 or 6")

    if len(hex_code) == 3:
        hex_code = ''.join([c * 2 for c in hex_code])

    red = int(hex_code[0:2], 16)
    green = int(hex_code[2:4], 16)
    blue = int(hex_code[4:6], 16)

    return (red, green, blue)


def rgb2hex(rgb: list[int]) -> str:
    return f"#{''.join(f'{x:02x}' for x in rgb)}"
