import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Fake training data (for learning)
X = np.array([
    [90, 40, 40, 20, 80, 6.5, 200],
    [60, 35, 30, 25, 70, 6.0, 150],
    [100, 50, 50, 18, 90, 7.0, 220]
])

y = np.array(["Rice", "Wheat", "Sugarcane"])

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model created!")
