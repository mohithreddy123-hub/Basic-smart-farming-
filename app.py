from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Convert inputs to float
        data = [float(x) for x in request.form.values() if x.strip() != ""]

        # Check if all fields are filled
        if len(data) != 7:
            return render_template("index.html", prediction_text="⚠️ Please enter all values.")

        final_input = np.array([data])
        prediction = model.predict(final_input)

        return render_template(
            "index.html",
            prediction_text=f"Recommended Crop: {prediction[0]}"
        )

    except ValueError:
        return render_template("index.html", prediction_text="⚠️ Invalid input. Enter numbers only.")

if __name__ == "__main__":
    app.run(debug=True)
