# 🖐️ Hand Gesture Cursor Project

An innovative application of computer vision that allows you to control your computer's cursor using hand gestures with Python. This project demonstrates an intuitive human-computer interface using MediaPipe for hand tracking and OpenCV for computer vision.

## Features

- **Real-time Hand Tracking**: Uses MediaPipe for accurate hand landmark detection
- **Cursor Movement**: Control cursor movement with your index finger
- **Click Gestures**: Perform left clicks by pinching thumb and index finger together
- **Smooth Movement**: Configurable smoothing for natural cursor control
- **Visual Feedback**: Live camera feed with hand landmarks and instructions
- **Easy Exit**: Press 'q' or move mouse to top-left corner to quit

## Requirements

- Python 3.7 or higher
- Webcam/Camera
- Windows/macOS/Linux

## Testing

Before running the main application, you can test the core logic:

```bash
python test_logic.py
```

This will verify that all the mathematical calculations and configurations are working correctly without requiring camera access or external dependencies.

To test hand tracking without cursor control:
```bash
python demo.py
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/salkeomkar578-lab/Hand-Gesture-Cursor-Project.git
cd Hand-Gesture-Cursor-Project
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Or use the setup script for guided installation:
```bash
python setup.py
```

## Usage

1. Run the main script:
```bash
python hand_gesture_cursor.py
```

2. Position your hand in front of the camera
3. Move your index finger to control the cursor
4. Pinch your thumb and index finger together to perform a left click
5. Press 'q' to quit the application

## Hand Gestures

| Gesture | Action |
|---------|--------|
| Index finger movement | Move cursor |
| Thumb + Index finger pinch | Left click |
| Press 'q' key | Exit application |

## Configuration

You can modify settings in `config.py`:

- `SMOOTHENING_FACTOR`: Adjust cursor movement smoothness (1-10)
- `CLICK_THRESHOLD`: Distance threshold for click detection (pixels)
- `CLICK_COOLDOWN`: Time between clicks (seconds)
- Camera resolution and detection confidence levels

## Troubleshooting

**Camera not working:**
- Ensure your camera is connected and not being used by other applications
- Try changing the camera index in the code (0, 1, 2, etc.)

**Poor hand detection:**
- Ensure good lighting conditions
- Keep your hand clearly visible in the camera frame
- Adjust `MIN_DETECTION_CONFIDENCE` in config.py

**Cursor movement too sensitive/slow:**
- Adjust `SMOOTHENING_FACTOR` in config.py
- Higher values = smoother but slower movement

## Technical Details

- **MediaPipe**: Google's framework for building perception pipelines
- **OpenCV**: Computer vision library for camera capture and image processing
- **PyAutoGUI**: Library for programmatic control of mouse and keyboard
- **Hand Landmarks**: Uses 21 key points of hand structure for tracking

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google MediaPipe team for the hand tracking solution
- OpenCV community for computer vision tools
- PyAutoGUI developers for mouse control functionality

## Future Enhancements

- [ ] Right-click gestures
- [ ] Scroll gestures
- [ ] Multi-hand support
- [ ] Gesture customization
- [ ] Voice commands integration
- [ ] Performance optimizations
