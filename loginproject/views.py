from django.shortcuts import render

from loginapp.forms import UserRegistrationForm



def index(request):
    return render(request,"index.html",{})


def logout(request):
    return render(request, 'index.html', {})

def UserLogin(request):
    return render(request, 'UserLogin.html', {})