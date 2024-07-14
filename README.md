# Invisible Cloak Effect using OpenCV

This Python script utilizes OpenCV to create an invisible cloak effect using a webcam. It captures the background, detects a specific color (strong blue by default), creates a mask around that color in real-time, and replaces it with the captured background, giving the appearance of invisibility.

<div align="center">
  <img src="https://media1.tenor.com/m/v3U9VngXSgMAAAAd/harry-potter-invisible.gif">
</div>

## Features

- Captures the background image to use for masking.
- Detects and masks a specific color (strong blue) from the live camera feed.
- Toggles the masking effect using keyboard input ('x').
- Press 'q' to quit the application.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Stremlit (`streamlit`)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install required Python packages:
   ```bash
   pip install opencv-python numpy
   ```

## Usage

1. Run the script:
   ```bash
   python cloaker.py
   ```

**OR**

2. Run the streamlit web app:
   ```bash
   streamlit run cloaker.py
   ```
   
3. Follow the on-screen instructions:
   - Move away from the camera during background capture (5-second countdown).
   - Press 'x' to toggle the invisible cloak effect on/off.
   - Press 'q' to quit the application.

## Customization

- Modify `lower_bound` and `upper_bound` in `main()` function to detect different colors.
- Adjust `num_frames` in `capture_background()` function for better background capture.

## Notes

- Ensure your webcam is connected and accessible.
- This script provides a basic implementation. Advanced features like real-time video streaming to a web app can be implemented using frameworks like Flask or Django.

## Contact Me

- Twitter: [@arindal_17](https://twitter.com/arindal_17)
- GitHub: [arindal1](https://github.com/arindal1)
- LinkedIn: [Arindal Char](https://www.linkedin.com/in/arindalchar)

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Keep Coding! 🚀
