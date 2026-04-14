import pandas as pd
import numpy as np
from scipy import optimize
import json

def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Please use CSV or JSON.")

def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def noise_filter(data, threshold=0.1):
    return data[data > threshold]

def baseline_correction(data):
    baseline = np.min(data)
    return data - baseline

def fit_calibration_curve(concentration, absorbance):
    def model(x, a, b):
        return a * x + b  # Simple linear model
    params, _ = optimize.curve_fit(model, concentration, absorbance)
    return params

def predict_concentration(model_params, absorbance):
    a, b = model_params
    concentration = (absorbance - b) / a
    return concentration

def run_pipeline(file_path):
    data = load_data(file_path)
    absorbance = normalize_data(data['absorbance'])
    absorbance = noise_filter(absorbance)
    absorbance = baseline_correction(absorbance)
    
    concentration = data['concentration']
    model_params = fit_calibration_curve(concentration, absorbance)
    
    predicted_concentration = predict_concentration(model_params, absorbance)
    
    return predicted_concentration

if __name__ == "__main__":
    file_path = 'data/input_data.csv'  # Example input path
    results = run_pipeline(file_path)
    print("Predicted Concentrations:", results)