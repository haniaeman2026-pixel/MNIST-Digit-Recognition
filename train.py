import os
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# ==========================================
# Create Model Folder
# ==========================================

os.makedirs("model", exist_ok=True)

# ==========================================
# Load MNIST Dataset
# ==========================================

print("=" * 50)
print("Loading MNIST Dataset...")
print("=" * 50)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(f"Training Images : {X_train.shape}")
print(f"Testing Images  : {X_test.shape}")

# ==========================================
# Data Preprocessing
# ==========================================

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# ==========================================
# Build CNN Model
# ==========================================

print("\nBuilding CNN Model...")

model = Sequential([

    Conv2D(
        32,
        (3,3),
        activation="relu",
        input_shape=(28,28,1)
    ),

    MaxPooling2D((2,2)),

    Conv2D(
        64,
        (3,3),
        activation="relu"
    ),

    MaxPooling2D((2,2)),

    Flatten(),

    Dense(
        128,
        activation="relu"
    ),

    Dropout(0.5),

    Dense(
        10,
        activation="softmax"
    )

])

# ==========================================
# Compile Model
# ==========================================

model.compile(

    optimizer="adam",

    loss="categorical_crossentropy",

    metrics=["accuracy"]

)

# ==========================================
# Train Model
# ==========================================

print("\nTraining Started...\n")

history = model.fit(

    X_train,

    y_train,

    validation_data=(X_test, y_test),

    epochs=5,

    batch_size=32,

    verbose=1

)

# ==========================================
# Evaluate Model
# ==========================================

loss, accuracy = model.evaluate(

    X_test,

    y_test,

    verbose=0

)

print("\n" + "=" * 50)
print(f"Test Accuracy : {accuracy*100:.2f}%")
print("=" * 50)

# ==========================================
# Save Model
# ==========================================

model.save("model/mnist_model.keras")

print("\nModel Saved Successfully!")
print("Location : model/mnist_model.keras")

print("\nProject Training Completed Successfully.")

import matplotlib.pyplot as plt

# ==========================================
# Accuracy Graph
# ==========================================

plt.figure(figsize=(8,5))

plt.plot(history.history["accuracy"], label="Training Accuracy")

plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.title("Model Accuracy")

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.legend()

plt.grid(True)

plt.savefig("model/accuracy.png")

plt.close()

# ==========================================
# Loss Graph
# ==========================================

plt.figure(figsize=(8,5))

plt.plot(history.history["loss"], label="Training Loss")

plt.plot(history.history["val_loss"], label="Validation Loss")

plt.title("Model Loss")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.legend()

plt.grid(True)

plt.savefig("model/loss.png")

plt.close()

print("Graphs Saved Successfully!")