from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users.objects.get(email=email)
        if user.email == email and user.password == password:
            return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Users.objects.create(
            name=name,
            phone_no=phone_no,
            email=email,
            password=make_password(password)
        )
    return render(request,'index.html')



