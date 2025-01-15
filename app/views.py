from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
import joblib
model = joblib.load('./savedmodel/rf_model.joblib')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        elif User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists!")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!")

    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def predict(request):
    return render(request, 'input.html')
def result(request):
    if request.method == 'POST':
            vegetable = request.POST['vegetable']
            season = request.POST['season']
            month =  request.POST['month']
            disaster =  request.POST['Disaster']
            condition=request.POST['condition']
            temperature =  request.POST['temperature']
            new_input = pd.DataFrame({
                'Vegetable':[vegetable.lower()],
                'Season': [season.lower()],
                'Month':[month.lower()],
                'Temp': [int(temperature)],
                'Deasaster Happen in last 3month': [disaster.lower()],
                'Vegetable condition': [condition.lower()]
                })
            print(new_input)
            predicted_pricerf = model.predict(new_input)
            print(predicted_pricerf[0])
            return render(request, 'result.html', {'result': round(predicted_pricerf[0], 2), 'vegetable': vegetable})

