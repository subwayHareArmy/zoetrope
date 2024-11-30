---

# Zoetrope Animation Generator

## **Motivation**
I've seen amazing zoetrope animations on binyl records on the internet and wanted to design my own.

Creating these traditionally involves a trial-and-error process, with physical prints, rotations, and camera setups. Found the process of designing quite cumbersome. 
This little script streamlines the testing of zoetrope animations digitally, enabling faster prototyping.

---

## **Process**
This script generates a **phenakistoscope animation** from a square input image by:
1. Extracting the central circular region.
2. Rotating the circular image into a defined number of frames (e.g., 24 for a full rotation).
3. Optionally looping the animation for a smoother playback experience.
4. Outputting the animation as an MP4 video file.

The generated video can be played to simulate a zoetrope effect or tested directly with physical setups.

---

## **How to Use**

1. **Dependencies**  

    Ensure you have the following Python libraries installed:
    - `Pillow` (for image processing)
    - `OpenCV` (for video creation)
    - `numpy` (for array manipulation)

    Install the dependencies with:
    ```bash
    pip install pillow opencv-python-headless numpy
    ```


2. **Input Image**  
   Use a square image (`.png` or `.jpg`) as input. The central circular region of the image will be used for the animation. 
   Place your input image (`diceGame.png`) in the same directory as the script.

   Example:
   - Filename: `diceGame.png`
   - Dimensions: 500x500 (or any square resolution)

3. **Script Execution**
   Run the script by passing the input image path:
   ```bash
   python createZoetropeAnimation.py
   ```
   
   By default:
   - The input file is named `diceGame.png`.
   - The output video file is generated as `diceGame_zoetrope_looped.mp4`.

---

## **Configuration**

The script provides the following customizable options:
- **Input Image Path**: Change `input_path` to your image's filename.
- **Output Video Path**: Automatically generated based on the input image name. Override if needed.
- **Number of Frames**: Default is `24` for a smooth animation.
- **Frames Per Second (FPS)**: Default is `12`. Adjust for faster or slower playback.
- **Loop Count**: Default is `5`. Increase for longer animations.

Example:
```python
create_phenakistoscope_animation(
    input_image_path="yourImage.png",
    output_video_path="yourImage_animation.mp4",
    num_frames=30,
    video_fps=24,
    loops=3
)
```

---

## **Output**
The script generates an MP4 video file, which you can preview directly or use in physical zoetrope setups.

---

Feel free to reach out if you are making zoetrope animations too, it's a fun time!