# ascii_conversion.py
gscale = "@%#*+=-:.  "  # 10 levels of gray, can be replaced by different character but if the amount of characters changes, code needs to be adapted

def convert_to_ascii(image) -> str:
    """Replaces pixel based on their brightness with character from gscale."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += gscale[pixel_value // 25]

    img_width = image.width
    ascii_art = "\n".join(ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width))
    
    return ascii_art