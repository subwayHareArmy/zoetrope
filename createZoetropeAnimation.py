import cv2
import numpy as np
from PIL import Image, ImageDraw

# Configs:
input_path = "diceGame.png"

def create_phenakistoscope_animation(input_image_path, output_video_path, num_frames=24, video_fps=24, loops=3):
    """
    Creates a phenakistoscope animation with logging and looping.

    Args:
        input_image_path (str): Path to the input image.
        output_video_path (str): Path to save the output video.
        num_frames (int): Number of frames in the animation.
        video_fps (int): Frames per second for the output video.
        loops (int): Number of times to loop the animation in the video.
    """
    # Step 1: Load the image
    img = Image.open(input_image_path).convert("RGBA")
    width, height = img.size
    radius = min(width, height) // 2
    print("Step 1 completed: Loaded image")

    # Step 2: Create a circular mask
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((width//2 - radius, height//2 - radius, width//2 + radius, height//2 + radius), fill=255)
    print("Step 2 completed: Created circular mask")

    # Step 3: Apply mask to extract circular region
    circular_image = Image.new("RGBA", (width, height))
    circular_image.paste(img, mask=mask)
    print("Step 3 completed: Applied mask to extract circular region")

    # Step 4: Prepare frames
    frames = []
    for i in range(num_frames):
        # Rotate the image
        rotated = circular_image.rotate(angle=i * (360 / num_frames), center=(width // 2, height // 2))
        frames.append(rotated)
    print(f"Step 4 completed: Prepared {num_frames} frames")

    # Step 5: Loop frames
    looped_frames = frames * loops
    print(f"Step 5 completed: Looped frames {loops} times (Total frames: {len(looped_frames)})")

    # Step 6: Determine video dimensions
    video_size = (width, height)
    print("Step 6 completed: Determined video dimensions")

    # Step 7: Create the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
    out = cv2.VideoWriter(output_video_path, fourcc, video_fps, video_size)
    print("Step 7 completed: Created video writer")

    # Step 8: Save each frame to the video
    for idx, frame in enumerate(looped_frames):
        # Convert PIL image to OpenCV format (BGR)
        frame_bgr = cv2.cvtColor(np.array(frame), cv2.COLOR_RGBA2BGR)
        out.write(frame_bgr)
        if idx % num_frames == 0:
            print(f"Progress: Saved frame {idx} of {len(looped_frames)}")
    print("Step 8 completed: Saved each frame to the video")

    out.release()
    print(f"Animation saved to {output_video_path}")
    print("Ran successfully! Exiting.")

# Usage
create_phenakistoscope_animation(
    input_image_path=input_path,
    output_video_path=input_path.rsplit('.', 1)[0] + "_zoetrope_looped.mp4",
    num_frames=24,
    video_fps=12,
    loops=5  # Number of times to loop the animation
)
