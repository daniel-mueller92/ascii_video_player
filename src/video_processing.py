# video_processing.py
import cv2
from PIL import Image
from alive_progress import alive_bar
from ascii_conversion import convert_to_ascii
from utils import find_terminal_size
from image_processing import grayscale_image, resize_image
import curses
import time

def frame_to_ascii(frame, terminal_dimensions: tuple[int, int]) -> str:
    """Convert a single frame to ASCII format."""
    image = Image.fromarray(frame)
    image = grayscale_image(image)
    image = resize_image(image, terminal_dimensions)
    return convert_to_ascii(image)

def video_to_ascii(video_path: str, terminal_dimensions: tuple[int, int]):
    """Converts multiple video frames to ASCII format.

    Progress bar is mostly there because I wanted to try it out and it looks nice.
    Saves each frame as an entry of the list 'frames'.    
    """
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames = []

    with alive_bar(total_frames, title="Processing video frames to ASCII") as bar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame_to_ascii(frame, terminal_dimensions))
            bar()
    cap.release()
    return frames

def process_video(file_path: str, fps: int = 24) -> None:
    """Main video processing.
    
    Calls all necessary helper functions in order to convert 
    and display video in ASCII.
    """
    terminal_dimensions = find_terminal_size()
    frames = video_to_ascii(file_path, terminal_dimensions)
    proceed = input("Done processing frames. Play video? (Y/N) ")
    if proceed.lower() == "y":
        frame_delay = 1 / fps
        curses.wrapper(lambda stdscr: play_ascii_frames(stdscr, frames, frame_delay))

def play_ascii_frames(stdscr, frames, frame_delay):
    """Helper function to use windows-curses. Only useful for Win-OS."""
    curses.curs_set(0)
    for frame in frames:
        stdscr.clear()
        stdscr.addstr(0, 0, frame)
        stdscr.refresh()
        time.sleep(frame_delay)
