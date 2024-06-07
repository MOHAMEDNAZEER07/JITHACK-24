from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

def input(request):
    return render(request, 'input2.0.html')

def crop(request):
    PATH = './notebook2/crop_recommendation.csv'
    df = pd.read_csv(PATH)
    features = df[['Nitrogen', 'Phosphorus','Potassium','temperature', 'humidity', 'ph', 'rainfall']]
    target = df['label']
    imputer = SimpleImputer(strategy='mean')
    imputed_features = imputer.fit_transform(features)
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(imputed_features, target, test_size=0.2, random_state=2)
    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    RF.fit(Xtrain, Ytrain)
    data=[]
    if request.method == 'POST':
        nitrogen = request.POST.get('Nitrogen')
        data.append(int(nitrogen))
        phosphorus = request.POST.get('Phosphorus')
        data.append(int(phosphorus))
        potassium = request.POST.get('Potassium')
        data.append(int(potassium))
        temperature = request.POST.get('temperature')
        data.append(float(temperature))
        humidity = request.POST.get('humidity')
        data.append(float(humidity))
        ph = request.POST.get('ph')
        data.append(float(ph))
        rainfall = request.POST.get('rainfall')
        data.append(float(rainfall))
    prediction = RF.predict([data])
    return render(request,'result3.html', {'result3': prediction[0].capitalize()})

