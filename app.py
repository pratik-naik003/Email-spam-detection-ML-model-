import streamlit as st
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Page config
st.set_page_config(page_title="Email Spam Detector", layout="centered")

# App title
st.title("📧 Email Spam Detection")
st.write("Enter an email message below to check whether it is **Spam** or **Not Spam**.")

# Text input
email_text = st.text_area("✉️ Email Content", height=200)

# Predict button
if st.button("Check Spam"):
    if email_text.strip() == "":
        st.warning("⚠️ Please enter email text")
    else:
        # Transform text
        text_vector = vectorizer.transform([email_text])

        # Prediction
        prediction = model.predict(text_vector)[0]

        # Output
        if prediction == 1:
            st.error("🚨 This email is **SPAM**")
        else:
            st.success("✅ This email is **NOT SPAM**")
