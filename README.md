# 🤖 AI Digit Recognition System

A professional Deep Learning project that recognizes handwritten digits (0–9) using a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**. The project includes a modern **Streamlit web application** where users can upload handwritten digit images and instantly receive predictions with confidence scores.

---

## 📌 Project Overview

The AI Digit Recognition System is a computer vision application developed using **TensorFlow**, **Keras**, and **Streamlit**. The model is trained on the famous MNIST handwritten digit dataset and predicts digits from uploaded images with high accuracy.

This project demonstrates the complete Machine Learning workflow, including:

- Data Loading
- Image Preprocessing
- CNN Model Training
- Model Evaluation
- Model Saving
- Web Application Deployment
- Real-Time Prediction

---

## ✨ Features

- 🔢 Recognizes handwritten digits (0–9)
- 🧠 CNN-based Deep Learning model
- 📤 Upload PNG, JPG, and JPEG images
- 🎯 Displays predicted digit
- 📊 Shows confidence score
- 📈 Probability chart for all digits
- 📱 Responsive Streamlit dashboard
- 🎨 Professional UI with custom CSS
- ⚡ Fast real-time prediction

---

## 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pillow
- Matplotlib
- Scikit-learn
- Pandas
- Streamlit

---

## 📂 Project Structure

```
MNIST-Digit-Recognition/
│
├── model/
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

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/MNIST-Digit-Recognition.git
```

### Move into Project Folder

```bash
cd MNIST-Digit-Recognition
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Train the Model

```bash
python train.py
```

The trained model will be saved inside:

```
model/mnist_model.keras
```

---

## ▶️ Run the Streamlit Application

```bash
streamlit run app.py
```

After running, the application will automatically open in your web browser.

---

## 📷 How to Use

1. Open the Streamlit application.
2. Upload a handwritten digit image.
3. Click **Predict Digit**.
4. View:
   - Predicted Digit
   - Confidence Score
   - Probability Chart
   - Model Performance

---

## 📊 Model Information

| Feature | Details |
|----------|---------|
| Model | Convolutional Neural Network (CNN) |
| Dataset | MNIST |
| Image Size | 28 × 28 Pixels |
| Classes | 10 (Digits 0–9) |
| Framework | TensorFlow/Keras |

---

## 📈 Future Improvements

- Drawing canvas for handwritten digits
- Dark/Light mode
- Prediction history
- Download prediction report
- Interactive charts
- Mobile-friendly dashboard

---

## 👩‍💻 Developed By

**Hania Eman**

AI & Data Science Student

---