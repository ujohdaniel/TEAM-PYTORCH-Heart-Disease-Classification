from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)
@app.route('/', methods= ['GET', 'POST'])
def predict():

    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        model_pred = model.predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    return render_template('index.html', model_pred=model_pred)


if __name__ == '__main__':
    app.run(debug= True)
