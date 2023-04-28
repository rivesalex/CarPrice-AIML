from flask import Flask, render_template, redirect, request
from app import app, Cars_Info, db
import pandas as pd
import os
from predict_ML import app, Cars

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Home.html')
def Home():
    return render_template('Home.html')

@app.route('/About.html')
def About():
    return render_template('About.html')

'''@app.route('/Cars.html')
def CARS():
    return render_template('Cars.html')
'''
@app.route('/Projects.html')
def Projects():
    return render_template('Projects.html')

@app.route('/test')
def PLOT():
    return render_template('test.html')

@app.route('/show_DB')
def showDB():
    cars = Cars_Info.query.all()
    if len(cars)<100:
        print(False)
        return render_template('show_DB.html',cars = cars)
    return render_template('show_DB_maxed.html',cars=len(cars))

@app.route('/reset_DB')
def resetDB():
    curdir = os.path.dirname(__file__)
    filepath = curdir + '/cars.db'

    # check if the cars.db is present:
    if not os.path.isfile(filepath):
        with app.app_context():
            db.create_all()

    df = pd.read_pickle('cleaned_cars_db.pickle')
    brands = df['manufacturer'].to_numpy()
    models = df['model1'].to_numpy()
    years = df['year'].to_numpy()
    mileages = df['odometer'].to_numpy()
    trims = df['trim'].to_numpy()
    prices = df['price'].to_numpy()

    for brand,model,year,mileage,trim,price in zip(brands,models,years,mileages,trims,prices):
        new_car = Cars_Info(brand=brand,model=model,year=year,
                            mileage=mileage,trim=trim,price=price)
        db.session.add(new_car)

    db.session.commit()

    return "DONE"