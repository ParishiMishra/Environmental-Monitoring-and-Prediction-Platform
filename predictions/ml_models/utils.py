import numpy as np
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the model
landslide_model = Sequential()
landslide_model.add(Dense(64, input_dim=3, activation='relu'))
landslide_model.add(Dense(32, activation='relu'))
landslide_model.add(Dense(1, activation='sigmoid'))

# Compile the model
landslide_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save the model
landslide_model.save('catalog.h5')

# Define the model
flood_model = Sequential()
flood_model.add(Dense(64, input_dim=2, activation='relu'))
flood_model.add(Dense(32, activation='relu'))
flood_model.add(Dense(1, activation='sigmoid'))

# Compile the model
flood_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save the model
flood_model.save('flood.h5')

# Load pre-trained models
try:
    landslide_model = load_model('catalog.h5')
    flood_model = load_model('flood.h5')
except Exception as e:
    print(f"Error loading models: {e}")
    raise  # Re-raise the exception to stop execution if models cannot be loaded

def predict_landslide(rainfall, soil_moisture, temperature):
    # Prepare input data for the model
    input_data = np.array([[rainfall, soil_moisture, temperature]])
    try:
        prediction = landslide_model.predict(input_data)
        risk_level = "high" if prediction[0][0] > 0.7 else "low"
        return risk_level, float(prediction[0][0])
    except Exception as e:
        print(f"Error predicting landslide: {e}")
        return None, None

def predict_flood(rainfall, river_level):
    # Prepare input data for the model
    input_data = np.array([[rainfall, river_level]])
    try:
        prediction = flood_model.predict(input_data)
        risk_level = "high" if prediction[0][0] > 0.7 else "low"
        return risk_level, float(prediction[0][0])
    except Exception as e:
        print(f"Error predicting flood: {e}")
        return None, None

# Test with sample data
landslide_risk = predict_landslide(100, 50, 30)
if landslide_risk[0] is not None:
    print(f"Landslide Risk: {landslide_risk}")
else:
    print("Failed to predict landslide risk.")

flood_risk = predict_flood(180,50)
if flood_risk[0] is not None:
    print(f"Flood Risk: {flood_risk}")
else:
    print("Failed to predict flood risk.")
