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
    N = int(request.form['N'])
    P = int(request.form['P'])
    K = int(request.form['K'])
    pH = float(request.form['pH'])

    input_features = np.array([[N, P, K, pH]])
    prediction = model.predict(input_features)
    crop = prediction[0]

    return render_template('index.html', prediction_text=f"🌱 Recommended Crop: {crop}")

if __name__ == '__main__':
    app.run(debug=True)
