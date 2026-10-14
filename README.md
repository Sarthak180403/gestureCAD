# GestureCAD — Gesture-Based CAD Inspection

**GestureCAD** is a computer vision project that aims to enable hands-free interaction with CAD models using hand gestures. The project uses a webcam to track hand movements and will progressively translate recognized gestures into commands for viewing and inspecting 3D CAD models.

**GitHub Repository:** [https://github.com/Sarthak180403/gestureCAD](https://github.com/Sarthak180403/gestureCAD)

The goal is to explore how gesture-based human-computer interaction can make engineering design inspection more intuitive.

> **Project status:** In development — currently focused on hand landmark detection and geometric analysis using OpenCV and MediaPipe.

## 🎯 Objectives

- Detect and track hand movements using a webcam.
- Identify and analyze the 21 hand landmarks provided by MediaPipe.
- Extract fingertip coordinates and study relationships between landmarks.
- Develop finger-state detection and hand gesture recognition.
- Map recognized gestures to interaction commands.
- Integrate gesture controls with 3D CAD model visualization.
- Explore gesture-based CAD inspection and manipulation.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam capture, image processing, and visualization |
| MediaPipe Hands | Hand detection and landmark tracking |
| NumPy | Numerical operations as needed |
| VS Code | Development environment |

## ⚙️ Current Implementation

The project currently includes the following functionality:

- Webcam video capture using OpenCV.
- Real-time hand detection using MediaPipe.
- Visualization of the hand's 21 landmarks and connections.
- Access to individual landmark IDs.
- Identification of the five fingertips:
  - Thumb: landmark 4
  - Index: landmark 8
  - Middle: landmark 12
  - Ring: landmark 16
  - Pinky: landmark 20
- Conversion of normalized landmark coordinates into image pixel coordinates.
- Visualization of selected fingertip positions using circles.
- Initial experiments comparing the positions of index-finger landmarks.

These features establish the foundation for subsequent gesture recognition and CAD interaction.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sarthak180403/gestureCAD.git
cd gestureCAD
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install opencv-python mediapipe
```

### 4. Run the application

If your main Python script is named `main.py`, run:

```bash
python main.py
```

Make sure your webcam is connected and that Python has permission to access it.

Press **`q`** to close the webcam window.

*Note: Replace `main.py` with the actual filename of your script if it is different.*

## 🧠 Understanding Hand Landmarks

MediaPipe Hands represents a detected hand using 21 anatomical landmarks.

Each landmark provides normalized `x` and `y` image coordinates and relative depth information through `z`.

For example:

```python
index_tip = hand.landmark[8]

x = index_tip.x
y = index_tip.y
z = index_tip.z
```

The normalized coordinates can be converted to pixel coordinates for visualization:

```python
h, w, _ = frame.shape

cx = int(index_tip.x * w)
cy = int(index_tip.y * h)
```

The resulting pixel coordinates can be used with OpenCV to draw points, lines, and other visual elements on the webcam frame.

## 🗺️ Development Roadmap

The project is being developed incrementally.

- Webcam initialization and frame capture
- Hand detection using MediaPipe
- Visualization of hand landmarks
- Access to individual landmarks
- Identification and marking of fingertips
- Initial landmark coordinate analysis
- Landmark distance and geometric analysis
- Finger-state detection
- Finger counting
- Basic gesture recognition
- Gesture-to-command mapping
- CAD model visualization and integration
- Gesture-based camera control
- CAD model manipulation and inspection
- End-to-end integration, testing, and demonstration

*The roadmap describes planned development as well as completed foundational work. Items will be marked complete as they are implemented and tested.*

## 🔮 Future Scope

The intended future direction is to integrate the hand-tracking system with a 3D visualization environment and CAD models.

Potential interactions include:

- Rotating a 3D model using hand gestures.
- Zooming and panning the model view.
- Selecting predefined inspection commands.
- Navigating around a model without relying exclusively on a mouse or keyboard.

These are planned capabilities and are not yet part of the current implementation.

## 📚 Learning Focus

This project is also an exploration of the concepts behind gesture-based interaction, including:

- Computer vision and real-time video processing.
- Hand landmark geometry.
- Coordinate systems and transformations.
- Geometric rules for gesture recognition.
- Human-computer interaction.
- Integration of computer vision with 3D CAD visualization.

## 👨‍💻 Author

**Sarthak Gupta**

- GitHub Profile: [@Sarthak180403](https://github.com/Sarthak180403)
- Project Repository: [GestureCAD](https://github.com/Sarthak180403/gestureCAD)

## 📌 Project Status

GestureCAD is an ongoing learning and development project. The current emphasis is on building a reliable understanding of hand tracking and landmark geometry before progressing to gesture recognition and CAD integration.

Contributions, suggestions, and feedback are welcome.

---

**GestureCAD — From Hand Tracking to Gesture-Based CAD Interaction.**
