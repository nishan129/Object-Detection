# Object-Detection

### Introduction
The real-time detection of helmet violations and capturing bike numbers from number plates is a comprehensive project that aims to enhance road safety by addressing two critical aspects:
1. Helmet Violation Detection: This component of the project focuses on identifying motorcycle riders who are not wearing helmets. It uses computer vision techniques to analyze real-time camera feeds and instantly alerts authorities when a violation is detected.
2. Capturing Bike Numbers: The second component involves recognizing number plates and extracting number plate information from vehicles in real-time. This feature is valuable for law enforcement.

### Helmet Missing Detection
The helmet missing detection module uses computer vision object detection techniques to:
1. Detect faces and riders on motorcycles.
2. Determine whether the rider is wearing a helmet.
3. Trigger alerts or notifications when a violation is detected.

### Capturing Bike Numbers
The number plate recognition module uses Optical Character Recognition (OCR) techniques to:
1. Detect number plates on vehicles.
2. Recognize the characters and display the number plate information in real-time.

### Dataset
-Acquired a comprehensive dataset from online sources containing 120 images with complete rider information, including the rider, helmet presence, and visible number plate and annotated it.

Dataset: https://www.kaggle.com/datasets/aneesarom/rider-with-helmet-without-helmet-number-plate/data

## Archietecture Used
* YOLO
* OCR


If you find this project useful, kindly give it a star! ⭐️


## How to run:

```bash
conda create -p venv python==7.3 -y
```

```bash
conda activate venv
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

