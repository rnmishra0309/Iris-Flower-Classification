from flask import Flask, render_template, request, redirect
import joblib
import numpy as np
import os

# Loading the model
model = joblib.load('model.sav')

# initialisation
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if (request.method == 'POST'):
        sl = request.form['sepal-length']
        sw = request.form['sepal-width']
        pl = request.form['petal-length']
        pw = request.form['petal-width']
        data = np.array([[sl, sw, pl, pw]])
        
        pred = model.predict(data)
        result = pred[0][5:]
        return render_template('prediction.html', prediction = result.capitalize())
    
    elif (request.method == 'GET'):
        return redirect('/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)