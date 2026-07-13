import streamlit as st
from PIL import Image
from predict import predict_digit

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Digit Recognition Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD CSS
# ==========================================

with open("style.css", "r", encoding="utf-8") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero-container">

<h1>🤖 AI Digit Recognition Dashboard</h1>

<p>
Deep Learning • CNN • TensorFlow • Streamlit
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================
# TOP DASHBOARD CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
    <div class="dashboard-card">

    <h2>📚</h2>

    <h3>Dataset</h3>

    <p>MNIST</p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="dashboard-card">

    <h2>🧠</h2>

    <h3>Model</h3>

    <p>CNN</p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="dashboard-card">

    <h2>🎯</h2>

    <h3>Classes</h3>

    <p>10 Digits</p>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class="dashboard-card">

    <h2>⚡</h2>

    <h3>Framework</h3>

    <p>TensorFlow</p>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# MAIN LAYOUT
# ==========================================

left, right = st.columns([1.1, 1])

with left:

    st.markdown("""
    <div class="upload-box">
    <h2>📤 Upload Handwritten Digit</h2>
    <p>PNG • JPG • JPEG Supported</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.markdown("### 🖼 Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

with right:

    st.markdown("""
    <div class="prediction-box">
    <h2>🎯 AI Prediction</h2>
    <p>Click the button below to recognize the handwritten digit.</p>
    </div>
    """, unsafe_allow_html=True)

    if uploaded_file is not None:

        if st.button(
            "🚀 Predict Digit",
            use_container_width=True
        ):

            with st.spinner("🧠 AI is analyzing your image..."):

                digit, confidence, probabilities = predict_digit(image)
                            # ==========================================
            # PREDICTION RESULT
            # ==========================================

            st.success("✅ Prediction Completed Successfully!")

            st.write("")

            c1, c2 = st.columns(2)

            with c1:

                st.markdown("""
                <div class="result-card">
                <h3>🔢 Predicted Digit</h3>
                </div>
                """, unsafe_allow_html=True)

                st.metric(
                    label="Prediction",
                    value=str(digit)
                )

            with c2:

                st.markdown("""
                <div class="result-card">
                <h3>🎯 Confidence Score</h3>
                </div>
                """, unsafe_allow_html=True)

                st.metric(
                    label="Confidence",
                    value=f"{confidence:.2f}%"
                )

            st.write("")

            st.progress(confidence / 100)

            if confidence >= 99:

                st.success("🌟 Outstanding Prediction!")

                st.balloons()

            elif confidence >= 95:

                st.success("🎉 Excellent Confidence")

            elif confidence >= 85:

                st.info("👍 Good Prediction")

            else:

                st.warning("⚠ Confidence is Low")

            st.write("")

            st.markdown("## 📊 Prediction Probability")

            probability_chart = {
                str(i): float(probabilities[i] * 100)
                for i in range(10)
            }

            st.bar_chart(
                probability_chart,
                use_container_width=True
            )

            st.write("")

            st.markdown("---")

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🤖 AI Dashboard")

    st.markdown("---")

    st.markdown("### 📚 Project")

    st.success("MNIST Digit Recognition")

    st.markdown("### 🧠 Model")

    st.info("Convolutional Neural Network")

    st.markdown("### 📊 Dataset")

    st.success("MNIST")

    st.markdown("### 🎯 Classes")

    st.info("Digits 0 - 9")

    st.markdown("### ⚡ Framework")

    st.success("TensorFlow / Keras")

    st.markdown("---")

    st.markdown("### 💡 Tips")

    st.write("✔ Write the digit clearly")

    st.write("✔ White background")

    st.write("✔ Center the digit")

    st.write("✔ PNG/JPG Supported")

    st.markdown("---")

    st.success("🚀 AI & Data Science Project")
    # ==========================================
# ABOUT PROJECT
# ==========================================

st.markdown("---")

st.markdown("""
<div class="about-section">

<h2>📚 About This Project</h2>

<p>
This AI application uses a <b>Convolutional Neural Network (CNN)</b>
trained on the <b>MNIST Handwritten Digit Dataset</b>.
It can recognize handwritten digits from <b>0 to 9</b> with
high accuracy.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================
# MODEL PERFORMANCE
# ==========================================

st.write("")

st.subheader("📈 Model Performance")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Accuracy Graph")

    try:
        st.image(
            "model/accuracy.png",
            use_container_width=True
        )
    except:
        st.info("Run train.py to generate Accuracy Graph.")

with col2:

    st.markdown("### Loss Graph")

    try:
        st.image(
            "model/loss.png",
            use_container_width=True
        )
    except:
        st.info("Run train.py to generate Loss Graph.")

# ==========================================
# TECHNOLOGIES
# ==========================================

st.markdown("---")

st.subheader("🛠 Technologies Used")

a, b, c, d = st.columns(4)

with a:
    st.success("🐍 Python")

with b:
    st.success("🧠 TensorFlow")

with c:
    st.success("🎈 Streamlit")

with d:
    st.success("📷 Pillow")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""

<div class="footer">

<h2>🤖 AI Digit Recognition Dashboard</h2>

<p>

Developed by

<b>Hania Eman</b>

</p>

<p>

AI & Data Science Student

</p>

<p>

TensorFlow • CNN • Streamlit • Python

</p>

</div>

""", unsafe_allow_html=True)