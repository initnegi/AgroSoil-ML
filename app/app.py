from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorus'])
        K = int(request.form['potassium'])
        pH = float(request.form['ph'])

        input_features = np.array([[N, P, K, pH]])
        prediction = model.predict(input_features)
        crop = prediction[0]

        return render_template('index.html', prediction_text=f"🌱 Recommended Crop: {crop}")
    except Exception as e:
        return render_template('index.html', prediction_text="⚠️ An error occurred during prediction.")


if __name__ == '__main__':
    app.run(debug=True)
