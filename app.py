import streamlit as st
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# App title
#st.title-->Displays the main heading of your app
st.title("📧 Email Spam Detection")

#st.write-->Displays normal text or instructions
st.write("Enter an email message below to check whether it is **Spam** or **Not Spam**.")

# Text input
#st.text_input() -->for single line input
#st.text_area()-->used to take multi line input
email = st.text_area("✉️ Email Content", height=200)

# Predict button
# When the user clicks the "Check Spam" button
if st.button("Check Spam"):
    
    # Check if the email text is empty
    if email.strip() == "": 
        # Show a warning message
        st.warning("Please enter email ")
    else:
        # Convert email text into numbers
        text_vector = vectorizer.transform([email])

        # Predict using the trained model
        # Step 1: Use the trained model to predict
        result = model.predict(text_vector)

        # Step 2: Prediction comes as a list/array
        # Example output: [0] or [1]

        # Step 3: Get the first (actual) prediction
        prediction = result[0]

        # If prediction is 1, email is spam
        if prediction == 1:
            # Show spam message
            st.error("This email is **SPAM**")
        else:
             # Show not spam message
            st.success("This email is **NOT SPAM**")