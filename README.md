# Gesture Pilot - Hand Gesture Recognition for Application Control and Virtual Mouse

**Gesture Pilot** is a versatile project that utilizes hand gestures for controlling various applications, making interaction more intuitive and efficient. This project offers two modes of operation:

1. **With Jetson Nano**: Optimized for deployment on Jetson Nano (model P3450), leveraging its powerful AI capabilities and compact form factor.
2. **Without Jetson Nano**: A general version designed to run on standard desktop or laptop setups using a webcam.

## Features

- Hand Gesture Recognition: Detects and interprets hand gestures using OpenCV and MediaPipe.
- Application Control:
  -- Game Control: Use gestures to simulate directional key presses (up, down, left, right).
  -- Presentation Control: Navigate slides (next/previous), display pointer, draw, and erase.
  -- Gesture Play: Control playback (play, pause, skip, adjust volume), Audio across all OS.
  -- Virtual Mouse: Move the cursor, click, and drag using gestures.
- Multi-Platform Support:
  -- Jetson Nano Version: Optimized for hardware acceleration with OpenCV CUDA on JetPack 4.6.
  -- Desktop/Laptop Version: Runs on Python and standard hardware with ease.

## Technologies Used

- Programming Language: Python
- Libraries:
  -- OpenCV
  -- MediaPipe
  -- PyAutoGUI
  -- cvzone
  -- pynput
- Hardware (Optional):
  -- Jetson Nano (P3450) with CSI/USB camera
  -- Raspberry Pi camera for RTSP streaming (for Jetson Nano setup)

## Gesture Mapping

## Setup Instructions

### For Jetson Nano

1. Clone the repository:
   ```bash
   git clone https://github.com/JayKalbi/gesture-pilot.git
   cd gesture-pilot  
   ```

2. Install Dependencies:
  [Setup Guidance](https://github.com/JayKalbi/JetsonNano-OpenCV-Mediapipe-SetUP.git)

### Contributions

We welcome contributions! Whether you want to enhance gesture detection, add new features, or improve documentation, feel free to open issues or submit pull requests.

## Contributors

- [Jay Kalbi](https://github.com/JayKalbi)

- [Vraj Prajapati](https://github.com/vraj3125)

- Kartavya Patel

## License

This project is licensed under the [MIT](https://github.com/JayKalbi/Song-Recommendation-based-on-Facial-Expression/tree/main?tab=MIT-1-ov-file#) License.
