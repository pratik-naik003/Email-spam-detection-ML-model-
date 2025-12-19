import pickle

# 1. Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# 2. Take input and predict
new = input("Enter Your Email: ")
new_vec = vectorizer.transform([new])
y_pred = model.predict(new_vec)

if y_pred[0] == 1:
    print("❌ Spam Email")
else:
    print("✅ Not Spam Email")
