#  AI Digit Recognition System

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Deep Learning](https://img.shields.io/badge/Deep-Learning-purple?style=for-the-badge)
![CNN](https://img.shields.io/badge/Model-CNN-success?style=for-the-badge)

---

#  Overview

The **AI Digit Recognition System** is a Deep Learning application developed using **TensorFlow**, **Keras**, and **Streamlit** that recognizes handwritten digits (0–9) with high accuracy.

The application is powered by a **Convolutional Neural Network (CNN)** trained on the famous **MNIST handwritten digit dataset**. Users can upload handwritten digit images through an interactive web interface and instantly receive the predicted digit, confidence score, and probability distribution.

This project demonstrates the complete Deep Learning workflow, including data preprocessing, model training, evaluation, and deployment.

---

#  Key Features

✅ Automatic MNIST dataset download

✅ Image preprocessing pipeline

✅ CNN-based Deep Learning model

✅ Real-time handwritten digit recognition

✅ Confidence score prediction

✅ Probability visualization

✅ Professional Streamlit dashboard

✅ Modern responsive UI

✅ Model accuracy and loss graphs

✅ Easy deployment and GitHub ready

---

#  Application Preview

The application provides an elegant dashboard where users can:

- Upload handwritten digit images
- Preview uploaded images
- Predict digits instantly
- View confidence score
- Analyze probability distribution
- Explore model performance graphs

---

#  Deep Learning Architecture

The CNN model consists of:

- Conv2D Layer (32 Filters)
- MaxPooling2D
- Conv2D Layer (64 Filters)
- MaxPooling2D
- Flatten Layer
- Dense Layer (128 Neurons)
- Dropout Layer
- Softmax Output Layer

---

#  Project Structure

```text
MNIST-Digit-Recognition
│
├── model
│   ├── mnist_model.keras
│   ├── accuracy.png
│   └── loss.png
│
├── app.py
├── train.py
├── predict.py
├── style.css
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| TensorFlow | Deep Learning |
| Keras | CNN Model |
| Streamlit | Web Application |
| NumPy | Numerical Computing |
| Pillow | Image Processing |
| Matplotlib | Visualization |
| Scikit-learn | Machine Learning Utilities |
| Pandas | Data Processing |

---

#  Dataset

**Dataset Name:** MNIST Handwritten Digits

- 70,000 handwritten images
- 10 Classes (0–9)
- Image Size: 28 × 28 pixels
- Grayscale Images

The dataset is automatically downloaded using TensorFlow during training.

---

#  Installation

## Clone Repository

```bash
https://github.com/haniaeman2026-pixel/MNIST-Digit-Recognition.git
```

---

## Move to Project Folder

```bash
cd MNIST-Digit-Recognition
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Train the Model

```bash
python train.py
```

The trained CNN model will automatically be saved inside:

```text
model/mnist_model.keras
```

---

#  Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

#  How to Use

### Step 1

Run the Streamlit application.

### Step 2

Upload a handwritten digit image.

### Step 3

Click **Predict Digit**.

### Step 4

View:

- Predicted Digit
- Confidence Score
- Probability Chart
- Model Performance

---

#  Model Performance

The project automatically generates:

- Training Accuracy Graph
- Validation Accuracy Graph
- Training Loss Graph
- Validation Loss Graph

These graphs help visualize the learning performance of the CNN model.

---

#  Future Improvements

- Drawing Canvas for handwritten digits
- Dark Mode
- Light Mode
- Prediction History
- Download Prediction Report
- Interactive Charts
- Mobile Responsive Dashboard
- Multiple Language Support

---

#  Skills Demonstrated

- Deep Learning
- Computer Vision
- Image Classification
- CNN Architecture
- TensorFlow
- Keras
- Streamlit
- Data Preprocessing
- Model Deployment
- Python Programming

---

#  Developed By

## **Hania Eman**

**AI & Data Science Student**

Passionate about Artificial Intelligence, Deep Learning, Computer Vision, Machine Learning, and Data Science.

---

