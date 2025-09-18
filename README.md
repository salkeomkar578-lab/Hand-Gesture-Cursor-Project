# Hand Gesture Virtual Mouse

This project implements a virtual mouse control system using hand gestures captured through a webcam. It allows you to control your computer's mouse cursor by moving your index finger in front of the camera and perform clicks by bringing your thumb and index finger together.

## Recommended Version
- **Clean Stable Version** (hand_mouse_clean.py): This is the recommended version that provides clean finger and palm detection only, with a simplified visual interface.

## Features of the Clean Stable Version

- Clean finger and palm detection only (no unnecessary visual elements)
- Stable cursor movement with improved smoothing
- Simple visual interface focusing on hands only
- Double-click support
- Automatic webcam recovery
- Works with all Python versions (3.7+)
- No MediaPipe dependency
- Reliable ESC key handling
- Enhanced skin tone detection for better hand tracking

## Requirements

### Standard Version
- Python 3.7 to 3.12 (MediaPipe has compatibility issues with Python 3.13+)
- Webcam
- Libraries:
  - OpenCV
  - MediaPipe
  - PyAutoGUI
  - NumPy

### Enhanced Version
- Python 3.7 or higher (including 3.13+)
- Webcam
- Libraries:
  - OpenCV
  - PyAutoGUI
  - NumPy (no MediaPipe dependency)

## Installation

1. Clone or download this repository

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Standard Version (with MediaPipe)
1. Run the program:
   ```
   python hand_mouse.py
   ```

2. Position your hand in front of the webcam:
   - Move your index finger to control the mouse cursor
   - Bring your thumb and index finger tips close together to perform a left-click
   - Press ESC to exit the program

### Enhanced Version (Pure OpenCV)
1. Run the enhanced version:
   ```
   python hand_mouse_enhanced.py
   ```

2. Position your hand in front of the webcam:
   - Move your index finger to control the mouse cursor
   - Bring your thumb and index finger close together to perform a left-click
   - Quick double pinch for double-click
   - Press ESC or Q key to exit the program
   - Watch the click progress bar for visual feedback on click detection

## Customization

You can adjust the following parameters in the code:

- `smoothing`: Controls cursor movement smoothness (lower = smoother but more latency)
- `click_delay`: Minimum time between clicks (in seconds)
- `min_detection_confidence` & `min_tracking_confidence`: Adjust hand detection sensitivity
- Distance threshold for click detection (default is 40 pixels)

## Troubleshooting

- **Webcam Not Detected**: Ensure your webcam is properly connected and not being used by another application
- **Hand Detection Issues**: Adjust lighting conditions and ensure your hand is clearly visible
- **Cursor Sensitivity**: Modify the smoothing factor or interpolation ranges for better control

## License

This project is open-source and available for personal and educational use.

## Acknowledgments

- This project uses [MediaPipe](https://mediapipe.dev/) for hand tracking
- Mouse control implemented with [PyAutoGUI](https://pyautogui.readthedocs.io/)
- Computer vision capabilities provided by [OpenCV](https://opencv.org/)
