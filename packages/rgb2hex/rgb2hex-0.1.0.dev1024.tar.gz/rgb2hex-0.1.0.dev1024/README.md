# RGB2HEX

A simple Python library for converting between Hexadecimal and RGB color formats.

Features
- Convert Hex color codes to RGB format.
- Convert RGB format back to Hex color codes.

## Installation

To install the library via pip:

```bash
pip install rgb2hex
```

## Convert Hex to RGB

You can convert a hexadecimal color code to an RGB tuple like this:

```python
from rgb2hex import hex2rgb

# Example usage
hex_code = "#ff5733"
rgb = hex2rgb(hex_code)
print(rgb)  # Output: (255, 87, 51)
```

## Convert RGB to Hex
You can convert an RGB list to a hexadecimal color code:

```python
from rgb2hex import rgb2hex

# Example usage
rgb = [255, 87, 51]
hex_code = rgb2hex(rgb)
print(hex_code)  # Output: #ff5733
```

## Contributing
Feel free to open issues or submit pull requests if you'd like to contribute.

## License
This project is licensed under the MIT License.