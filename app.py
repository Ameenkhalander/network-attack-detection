from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    feature1 = float(request.form['feature1'])
    feature2 = float(request.form['feature2'])
    feature3 = float(request.form['feature3'])

    score = feature1 + feature2 + feature3

    if score > 50:
        result = "Potential Network Attack Detected"
    else:
        result = "Normal Network Traffic"

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
