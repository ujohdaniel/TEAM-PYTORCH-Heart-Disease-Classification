from flask import Flask, render_template, request, redirect, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
import model

app = Flask(__name__)
# app.config['SECRET_KEY']= 'antelisthebest'
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'
# db= SQLAlchemy(app)

# # Creating the tables of the database
# class Form(db.Model):
#     id= db.Column(db.Integer, primary_key=True, nullable=False)
#     fullname= db.Column(db.Text, nullable=False)
#     age= db.Column(db.Integer, nullable=False)
#     sex= db.Column(db.Text, nullable=False)
#     cp= db.Column(db.Integer, nullable=False)
#     trestbps= db.Column(db.Integer, nullable=False)
#     chol= db.Column(db.Integer, nullable=False)
#     fbs= db.Column(db.Integer, nullable=False)
#     restecg= db.Column(db.Integer, nullable=False)
#     thalach= db.Column(db.Integer, nullable=False)
#     exang= db.Column(db.Integer, nullable=False)
#     oldpeak= db.Column(db.Integer, nullable=False)
#     slope= db.Column(db.Integer, nullable=False)
#     ca= db.Column(db.Integer, nullable=False)
#     thal= db.Column(db.Integer, nullable=False)
#     date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


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