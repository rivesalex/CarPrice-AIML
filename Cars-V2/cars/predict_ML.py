# Load the current model:
from flask import render_template, request, redirect
from app import app, Cars_Info, db
import pandas as pd
import pickle
import numpy as np

from plotting_functions import getPlot

out_ML = pickle.load(open('data/out_ML.pkl','rb'))
brands = pd.read_pickle('data/brands.pkl')
Model = pickle.load(open('trained_models/ML_model.pkl','rb'))

brand_dict = {}
for i,brand in enumerate(brands):
    brand_dict[brand] = i

def createEntry(trim,year,odometer,price,make,brand_keys):
    if not make in brand_keys.keys():
        return 'Invalid Car Brand'
    
    makes = np.zeros(len(brand_keys))
    i = brand_keys[make]
    makes[i] = 1
    yp = np.array([trim,year,odometer,price])
    return np.concatenate([yp,makes]).reshape(1,-1)


# def getPlot(brand,mileage,year,df,year_range=1, mileage_range=15000,count=0):
df = pd.read_pickle('data/cleaned_cars_db.pickle')

'''
@app.route('/Cars.html',methods=('GET','POST'))
def get_plot():
    if request.method == 'POST':
            if request.form['brand'] != None:
                brand = request.form['brand']
                #model = request.form['model']
                year = request.form['year']
                mileage = request.form['mileage']
                getPlot(brand,int(mileage),int(year),df)
                print('Plotly Graph Generated')
                return render_template('Cars.html')
    return render_template('Cars.html')
'''
    

@app.route('/Cars.html',methods=('GET','POST'))
def Cars():
    # setting up logicals:

    if request.method == 'POST':
        print('True')
        if request.form['brand'] != None:
            print('running alrts')
            brand = request.form['brand']
            #model = request.form['model']
            year = request.form['year']
            mileage = request.form['mileage']
            price = request.form['price']
            trim = request.form['trim']
            new_car = Cars_Info(brand=brand, model = 'null',year=year, trim = trim,price=price, mileage=mileage)
            
            X = createEntry(trim,year,mileage,price,brand,brand_dict).astype(float)
            output = Model.predict(X)
            getPlot(brand,int(mileage),int(year),df)

            if output != 1:
                print('no way')
                alert_user=True
            if output == 1:
                alert_user=False

            if alert_user == True:
                print('trying to render')
                return render_template('Cars-Wrong-V2.html')
            
            db.session.add(new_car)
            db.session.commit()

        return render_template('Cars.html')
    return render_template('Cars.html')

@app.route('/Cars-Wrong-V2.html',methods=('GET','POST'))
def Cars_Wrong():
    # setting up logicals:

    if request.method == 'POST':
        print('True')
        if request.form['brand'] != None:
            print('running alrts')
            brand = request.form['brand']
            #model = request.form['model']
            year = request.form['year']
            mileage = request.form['mileage']
            price = request.form['price']
            trim = request.form['trim']
            new_car = Cars_Info(brand=brand, model = 'null',year=year, trim = trim,price=price, mileage=mileage)
            
            X = createEntry(trim,year,mileage,price,brand,brand_dict).astype(float)
            output = Model.predict(X)
            getPlot(brand,int(mileage),int(year),df)

            if output != 1:
                print('no way')
                alert_user=True
            if output == 1:
                alert_user=False

            if alert_user == True:
                print('trying to render')
                return render_template('Cars-Wrong-V2.html')
            
            db.session.add(new_car)
            db.session.commit()

        return render_template('Cars.html')
    return render_template('Cars-Wrong-V2.html')