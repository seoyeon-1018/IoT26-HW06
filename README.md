# IoT26-HW06 - Vehicle Detection with YOLO on Raspberry Pi

## 1. Objective

The objective of this assignment is to install YOLO on Raspberry Pi and detect a vehicle displayed on a computer monitor.

In this project, I installed Ultralytics YOLO on Raspberry Pi, captured a car image using the Raspberry Pi Camera, and detected the car using a YOLO model.

## 2. Hardware

- Raspberry Pi
- Raspberry Pi Camera
- microSD card
- Power supply
- PC or laptop
- Monitor displaying a car image

## 3. Software

- Raspberry Pi OS
- Python 3
- Python virtual environment
- Ultralytics YOLO
- YOLO11n model

## 4. Setup Process

### 4.1 Raspberry Pi Update

First, I updated the Raspberry Pi packages.

```bash
sudo apt update
sudo apt upgrade -y
```
### 4.2 Python Environment Setup

I installed the required Python packages and created a virtual environment for YOLO.

```bash
sudo apt install python3-pip python3-venv python3-full -y
python3 -m venv ~/yolo-env
source ~/yolo-env/bin/activate
pip install -U pip setuptools wheel
```

### 4.3 YOLO Installation

During the installation process, a storage-related error occurred because the temporary directory had limited space.

To solve this issue, I created a temporary folder in the home directory and used it as the temporary directory during installation.

```bash
mkdir -p ~/tmp
TMPDIR=$HOME/tmp pip install --no-cache-dir ultralytics
```

After the installation was completed, I checked the YOLO version.

```bash
yolo version
```

<img width="664" height="68" alt="01_yolo_version" src="https://github.com/user-attachments/assets/db27e3ed-8679-45e0-9f19-f86805a3c180" />


## 5. Camera Test

I used the Raspberry Pi Camera to capture an image of a car displayed on a computer monitor.

First, I created a folder to save the images for this assignment.

```bash
mkdir -p ~/Pictures/hw6_yolo
```

Then, I captured the car image using the Raspberry Pi Camera.

```bash
rpicam-still -o ~/Pictures/hw6_yolo/monitor_car.jpg --width 640 --height 480
```

The captured image was saved as `monitor_car.jpg`.

<img width="2879" height="1711" alt="02_captured_car" src="https://github.com/user-attachments/assets/5c9738e1-2119-4337-bb3c-e681b39373b3" />


## 6. YOLO Vehicle Detection Using Python

After capturing the image with the Raspberry Pi Camera, I used a Python script to run YOLO vehicle detection.

The Python code loads the YOLO model, analyzes the captured image, and saves the detection result image.

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(
    source="/home/iotteam2/Pictures/hw6_yolo/monitor_car.jpg",
    conf=0.25,
    save=True
)
```

The captured image was used as the input image for YOLO detection.

```bash
source ~/yolo-env/bin/activate
python detect_car.py
```

The YOLO model detected the vehicle in the image and saved the detection result.


<img width="2872" height="1710" alt="03_yolo_result" src="https://github.com/user-attachments/assets/df617d09-60e8-4438-b8a8-b566be65c371" />


## 7. Result

The Raspberry Pi Camera successfully captured the car image displayed on the computer monitor.

After running YOLO on the captured image, the model detected the vehicle successfully.

This confirms that YOLO was successfully installed and executed on Raspberry Pi.


