# main.py
import argparse
from image_processing import process_image
from video_processing import process_video

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    args = parser.parse_args()

    file_path = f"../files/{args.file_name}"

    if file_path.endswith(".jpg"):
        process_image(file_path)
    elif file_path.endswith(".mp4"):
        process_video(file_path, fps=24)
    else:
        print("Unsupported file format. Only .jpg and .mp4 are supported.")

if __name__ == "__main__":
    main()
