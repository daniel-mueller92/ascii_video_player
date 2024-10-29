# image_processing.py
from PIL import Image
import os
from ascii_conversion import convert_to_ascii
from utils import find_terminal_size

def load_image(file_path: str) -> Image.Image:
    """Load image from file."""
    # TODO: Other functions will not work if None is returned.
    try:
        return Image.open(file_path)
    except FileNotFoundError:
        print("Your specified file was not found...")
        return None

def grayscale_image(image: Image.Image) -> Image.Image:
    """Convert image to grayscale, as colored ASCII is not supported."""#
    # TODO: Think about adding color support.
    return image.convert('L')

def resize_image(image: Image.Image, terminal_dimensions: tuple[int, int]=None) -> Image.Image:
    """Resizes images to max terminal dimensions."""
    if terminal_dimensions:
        max_width = terminal_dimensions[0] - 1
        max_height = terminal_dimensions[1] - 1
        
        width, height = image.size
        aspect_ratio = width / height
        
        if width / max_width > height / max_height:
            new_width = max_width
            new_height = int(new_width / aspect_ratio)
        
        else:
            new_height = max_height
            new_width = int(new_height * aspect_ratio)
        return image.resize((new_width, new_height))
    
    return image

def save_ascii_to_txt(save_path: str, txt: str) -> None:
    """Saves converted image to file; not really needed anymore."""
    with open(save_path, "w") as f:
        f.write(txt)

def process_image(file_path: str) -> None:
    """Main image processing.
    
    Calls all necessary helper functions to load, convert and display image in ASCII.
    """
    terminal_dimensions = find_terminal_size()

    img = load_image(file_path)
    if img:
        img = grayscale_image(img)
        img = resize_image(img, terminal_dimensions)
        ascii_art = convert_to_ascii(img)
        save_ascii_to_txt("../files/ascii_art.txt", ascii_art)
        print(ascii_art)