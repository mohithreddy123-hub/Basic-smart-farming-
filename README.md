# Basic-smart-farming-# 🌱 Smart Farming – Crop Recommendation System

A Machine Learning based web application that recommends the most suitable crop to grow based on soil nutrients and environmental conditions. This project uses **Flask** for the backend and a **Random Forest Classifier** model for prediction.

---

## 🚀 Features

- Predicts the best crop using Machine Learning  
- Simple and user-friendly web interface  
- Fast predictions using a trained model  
- Built with Python, Flask, and Scikit-learn  

---

## 🧠 How It Works

The model is trained using agricultural parameters such as:

- Nitrogen  
- Phosphorus  
- Potassium  
- Temperature  
- Humidity  
- Soil pH  
- Rainfall  

After training, the model is saved as `model.pkl` and loaded into the Flask application to generate predictions.

---

## 🏗️ Project Structure
│
├── app.py # Flask application<br>
├── model.py # Model training script<br>
├── model.pkl # Saved ML model<br>
├── templates/<br>
│ └── index.html # Frontend UI<br>
├── requirements.txt<br>
└── README.md<br>


---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/smart-farming.git
cd smart-farming

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Project
✅ Step 1 — Train the Model (Only if model.pkl is missing)
python model.py

✅ Step 2 — Start the Flask Server
python app.py


Now open your browser and go to:

http://127.0.0.1:5000/

🖥️ Usage

Enter soil nutrient values and environmental conditions.

Click Predict.

The system will recommend the most suitable crop.

🛠️ Tech Stack

Python

Flask

Scikit-learn

NumPy

HTML

📈 Future Improvements

Train the model using a real-world agricultural dataset

Enhance UI with CSS / Bootstrap

Deploy the project on cloud platforms (AWS, Render, Heroku)

Add more crop varieties for prediction

Convert the application into a REST API
