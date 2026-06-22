# Multimodal Human-Computer Interaction System using Head Movement, Eye Blink Detection, and Voice Commands

## Overview

The Multimodal Human-Computer Interaction (HCI) System is an intelligent assistive technology platform that enables users to interact with a computer without using traditional input devices such as a mouse or keyboard.

The system integrates:

* Head Movement Tracking
* Eye Blink Detection
* Voice Command Recognition
* Real-Time Cursor Control

to provide a hands-free and accessible computing experience.

The proposed framework combines computer vision, facial landmark detection, speech recognition, and automation technologies to improve accessibility and user interaction efficiency.

---

## Problem Statement

Traditional computer systems primarily rely on physical input devices such as keyboards and mice. These devices may not be suitable for:

* Individuals with physical disabilities
* Users with limited motor abilities
* Hands-free environments
* Accessibility-focused applications

This project addresses these limitations by developing a multimodal interaction system that allows users to control a computer using facial movements, eye blinks, and voice commands.

---

## Objectives

The primary objectives of this project are:

* Enable hands-free computer interaction
* Control cursor movement through head tracking
* Perform mouse clicks using eye blinks
* Support voice-based commands for navigation and actions
* Provide audio feedback for user actions
* Improve accessibility and usability
* Create a real-time multimodal interaction environment

---

## Features

### Head-Based Cursor Control

* Real-time face tracking using MediaPipe Face Landmarker
* Nose landmark tracking for cursor movement
* Smooth cursor navigation through coordinate smoothing

### Eye Blink Detection

* Automatic Eye Aspect Ratio (EAR) calibration
* Single blink detection for mouse click
* Long blink detection for double-click

### Voice Control Module

Supported voice commands include:

* Left
* Right
* Up
* Down
* Click
* Double Click
* Pause
* Resume
* Stop

### Audio Feedback System

Provides spoken feedback for:

* System startup
* Calibration completion
* Single click
* Double click
* Pause and resume operations
* System shutdown

### Real-Time Interaction

* Simultaneous head, eye, and voice control
* Parallel execution using multithreading
* Low-latency user interaction

---

## Tech Stack

### Programming Language

* Python

### Computer Vision

* OpenCV
* MediaPipe Face Landmarker

### Automation

* PyAutoGUI

### Speech Processing

* SpeechRecognition
* SoundDevice

### Text-to-Speech

* pyttsx3

### Supporting Libraries

* NumPy
* Threading
* Time

---

## System Architecture

The system consists of the following modules:

### User Interaction Module

Captures facial movements, eye blinks, and voice commands.

### Face Tracking Module

Detects facial landmarks and extracts head movement information.

### Blink Detection Module

Calculates Eye Aspect Ratio (EAR) and identifies blink patterns.

### Voice Recognition Module

Processes microphone input and recognizes predefined commands.

### Cursor Control Module

Maps head and voice inputs to cursor movement actions.

### Click Control Module

Performs mouse click and double-click operations.

### Audio Feedback Module

Provides spoken responses to user actions.

---

## Architecture Workflow

1. The webcam captures live video frames.
2. MediaPipe detects facial landmarks.
3. Nose coordinates are extracted and mapped to screen coordinates.
4. Cursor position is updated based on head movement.
5. Eye landmarks are used to calculate the Eye Aspect Ratio (EAR).
6. Blink patterns are analyzed to perform click operations.
7. Voice commands are captured through the microphone.
8. Speech recognition converts voice to text commands.
9. Commands are translated into cursor actions.
10. Audio feedback confirms executed actions.
11. The system continuously processes inputs in real time.

---

## Facial Landmark Tracking

The system uses MediaPipe Face Landmarker to identify key facial landmarks including:

* Nose tip
* Eye corners
* Eyelids
* Facial contours

These landmarks are used for:

* Head tracking
* Cursor navigation
* Blink detection

---

## Eye Aspect Ratio (EAR)

Eye Aspect Ratio is used for blink detection.

Formula:

EAR = Vertical Eye Distance / Horizontal Eye Distance

The system performs automatic calibration during startup to determine an appropriate blink threshold for each user.

---

## Voice Recognition Module

The voice recognition module allows users to control the system through speech.

### Supported Commands

| Voice Command | Action            |
| ------------- | ----------------- |
| Left          | Move Cursor Left  |
| Right         | Move Cursor Right |
| Up            | Move Cursor Up    |
| Down          | Move Cursor Down  |
| Click         | Single Click      |
| Double Click  | Double Click      |
| Pause         | Pause Tracking    |
| Resume        | Resume Tracking   |
| Stop          | Exit Application  |

---

## How the System Works

1. The user starts the application.
2. The webcam and microphone are initialized.
3. Facial landmark detection begins.
4. Automatic EAR calibration is performed.
5. Head movements control cursor navigation.
6. Eye blinks trigger click actions.
7. Voice commands provide additional cursor and system control.
8. Audio feedback confirms system actions.
9. The user interacts with the computer without using physical input devices.

---

## Project Modules

### 1. Face Tracking Module

Tracks facial landmarks and head movement.

### 2. Cursor Navigation Module

Maps head movement to screen coordinates.

### 3. Blink Detection Module

Detects eye blinks and performs click actions.

### 4. Voice Control Module

Processes microphone input and executes commands.

### 5. Audio Feedback Module

Provides spoken system responses.

### 6. System Control Module

Handles pause, resume, and shutdown operations.

---

## Performance Evaluation

### Blink Detection Confusion Matrix

| Actual / Predicted | Blink Detected | No Blink Detected |
| ------------------ | -------------- | ----------------- |
| Actual Blink       | 47             | 3                 |
| Actual No Blink    | 4              | 46                |

### Performance Metrics

#### Accuracy

93%

#### Precision

92.15%

#### Recall

94%

---

## Benefits of the System

* Hands-free computer interaction
* Improved accessibility
* Reduced dependency on physical devices
* Real-time operation
* Personalized user calibration
* Multimodal interaction support
* Enhanced user experience

---

## Future Enhancements

Possible future improvements include:

* Gesture-based scrolling
* Drag-and-drop through facial gestures
* Multi-language voice support
* Emotion recognition
* AI-based adaptive calibration
* Cloud-based deployment
* Mobile application support
* Deep learning-based blink detection

---

## Research Contribution

The proposed system integrates:

* Facial Landmark Tracking
* Eye Blink Detection
* Voice Recognition
* Cursor Automation

to create an intelligent multimodal human-computer interaction environment suitable for accessibility-focused applications and next-generation computing interfaces.

---

## Project Team

**D. Srichandana**

B.Tech – Computer Science and Engineering (Artificial Intelligence and Machine Learning)

Vardhaman College of Engineering

---

## Guide

Faculty Guide

Department of Computer Science and Engineering

Vardhaman College of Engineering

---

## Institution

Department of Computer Science and Engineering

Vardhaman College of Engineering

Hyderabad, Telangana, India

---

## Repository Structure

Multimodal-HCI-System/

│── src/

│── models/

│── voice_control/

│── blink_detection/

│── head_tracking/

│── assets/

│── docs/

│── face_landmarker.task

│── requirements.txt

│── README.md

---

## Installation and Setup

### Prerequisites

Make sure the following are installed:

* Python 3.10+
* Webcam
* Microphone
* Git

### Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui pyttsx3 SpeechRecognition sounddevice
```

### Download Model

Download:

face_landmarker.task

Place it in the project root directory.

### Run Application

```bash
python main.py
```

---

## Contact

For academic, research, or project-related queries, please contact the Department of Computer Science and Engineering, Vardhaman College of Engineering.

---

## Conclusion

The Multimodal Human-Computer Interaction System successfully combines head movement tracking, eye blink detection, and voice recognition to create a hands-free computing environment.

By integrating computer vision and speech technologies, the system:

* Improves accessibility
* Enables natural interaction
* Reduces dependency on traditional input devices
* Provides real-time multimodal control

This makes the system a promising solution for assistive technologies and future intelligent human-computer interaction platforms.
