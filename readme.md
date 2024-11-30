### `README.md`

---

# Phenakistoscope Animation Generator

## **Motivation**

The **phenakistoscope** is an early animation device that creates the illusion of motion through the rapid succession of images on a spinning disc. It’s an exciting intersection of art, physics, and visual storytelling. In this project, we aim to modernize this classic animation concept by digitizing and automating the creation process.

Printing physical discs, testing them manually, and adjusting designs through trial-and-error can be time-consuming and labor-intensive. This project offers a streamlined way to emulate, test, and iterate phenakistoscope designs digitally before committing them to a physical medium.

---

## **The Need for This Project**

- **Automation**: Avoid repetitive physical printing and testing by validating designs digitally.
- **Customization**: Quickly generate animations with any input design and desired number of frames.
- **Cost Efficiency**: Save time and resources by ensuring the animation works as intended before printing.
- **Preservation**: Bring a timeless art form into the digital age, making it accessible to anyone with a computer.

---

## **What This Code Does**

This Python script:
1. **Processes a square image**: Extracts the central circular region to simulate the spinning disc.
2. **Creates animation frames**: Rotates the circular region incrementally based on the number of frames specified.
3. **Loops animations**: Allows repeating the animation for extended video durations.
4. **Generates an MP4 video**: Compiles all frames into a seamless video to preview the animation effect.

---

## **How to Use**

### **1. Prerequisites**

Ensure you have the following installed:
- Python 3.8 or later
- Required Python libraries: `Pillow`, `opencv-python-headless`, and `numpy`.

Install these dependencies using:
```bash
pip install pillow opencv-python-headless numpy
```

---

### **2. Preparing Your Image**

1. **Input Image Requirements**:
   - The image must be **square** (e.g., 512x512, 1024x1024).
   - The animation works best if the central circular region contains the design you want animated.

2. **Place the image**:
   - Save your image in the same directory as the script, or provide the full path to it in the `input_path` variable.

---

### **3. Running the Script**

Edit the script's configuration:
- Set `input_path` to your image file (e.g., `"vanishingAct.png"`).
- Customize parameters such as:
  - `num_frames`: Number of frames in the animation.
  - `video_fps`: Frames per second of the output video.
  - `loops`: Number of times the animation is repeated in the video.

Run the script:
```bash
python phenakistoscope_animation.py
```

---

### **4. Output**

- The script generates an MP4 video in the same directory as the input image.
- The video will have a name based on the input image file, such as `vanishingAct_zoetrope_looped.mp4`.

---

## **Dependencies**

The project uses the following libraries:
- **Pillow**: For image manipulation.
- **OpenCV**: For video creation.
- **NumPy**: For efficient array processing.

Install all dependencies using:
```bash
pip install pillow opencv-python-headless numpy
```

---

## **Folder Structure**

```
project/
│
├── phenakistoscope_animation.py   # Main script
├── vanishingAct.png               # Example input image (replace with your own)
├── vanishingAct_zoetrope_looped.mp4  # Generated video (output)
├── README.md                      # This readme file
```

---

## **Customizations**

- **Input Image**: Change `input_path` to test with different designs.
- **Number of Frames**: Adjust `num_frames` to control animation smoothness.
- **Loops**: Modify `loops` to extend video duration.
- **Output Video Name**: The name is auto-generated but can be manually changed.

---

## **Troubleshooting**

- **Video Too Short?** Increase the `loops` parameter.
- **Animation Not Smooth?** Increase `num_frames` for finer rotations.
- **Errors?**
  - Ensure the input image is a valid square image.
  - Verify all required dependencies are installed.

---

## **Contributing**

Contributions to improve this project are welcome! Feel free to:
- Optimize the script.
- Add features like custom masks or live previews.
- Share your creations!

Fork the repo, make your changes, and submit a pull request.

---

## **License**

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## **Acknowledgments**

This project is inspired by the timeless artistry of phenakistoscopes and the desire to preserve and modernize classic animation techniques. Thank you to the open-source community for providing the tools to make this possible.

--- 

Enjoy creating mesmerizing animations!