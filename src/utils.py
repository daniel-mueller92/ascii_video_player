# utils.py
import shutil

def find_terminal_size() -> tuple[int, int]:
    """Determines terminal size, as it is the limiting factor for displaying a video in ASCII."""
    terminal_size = shutil.get_terminal_size()
    print("Terminal dimensions:", terminal_size.lines, terminal_size.columns)
    return terminal_size.columns, terminal_size.lines