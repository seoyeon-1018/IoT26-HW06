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


## 6. YOLO Vehicle Detection

After capturing the image, I used YOLO to detect the car in the image.

```bash
source ~/yolo-env/bin/activate
yolo predict model=yolo11n.pt source=~/Pictures/hw6_yolo/monitor_car.jpg
```

The YOLO model detected the vehicle and saved the detection result image in the `runs/detect/` folder.

<img width="2872" height="1710" alt="03_yolo_result" src="https://github.com/user-attachments/assets/df617d09-60e8-4438-b8a8-b566be65c371" />


## 7. Result

The Raspberry Pi Camera successfully captured the car image displayed on the computer monitor.

After running YOLO on the captured image, the model detected the vehicle successfully.

This confirms that YOLO was successfully installed and executed on Raspberry Pi.

## 8. What I Learned

Through this assignment, I learned how to install YOLO on Raspberry Pi and run object detection using a YOLO model.

I also learned how to create a Python virtual environment, install required Python packages, and use the Raspberry Pi Camera to capture an image.

During the installation process, I encountered a storage-related error. I solved this issue by changing the temporary directory to a folder inside the home directory.

This project helped me understand how Raspberry Pi can be used for computer vision and IoT-based image recognition tasks.
