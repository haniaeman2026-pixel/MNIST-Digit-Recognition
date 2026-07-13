import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# ==========================================
# Load Trained Model
# ==========================================

MODEL_PATH = "model/mnist_model.keras"

model = load_model(MODEL_PATH)

# ==========================================
# Image Preprocessing
# ==========================================

def preprocess_image(image):

    # Convert to grayscale
    image = image.convert("L")

    # Resize image
    image = image.resize((28, 28))

    # Convert to NumPy array
    img = np.array(image)

    # Invert colors (MNIST format)
    img = 255 - img

    # Normalize
    img = img.astype("float32") / 255.0

    # Reshape for CNN
    img = img.reshape(1, 28, 28, 1)

    return img

# ==========================================
# Prediction Function
# ==========================================

def predict_digit(image):

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image, verbose=0)

    predicted_digit = int(np.argmax(prediction))

    confidence = float(np.max(prediction) * 100)

    probabilities = prediction[0]

    return predicted_digit, confidence, probabilities