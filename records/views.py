from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from django.contrib.auth.models import Group

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'records/login.html', {'error': 'Invalid credentials'})
    return render(request, 'records/login.html')

@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'records/dashboard.html', {'students': students})

def user_logout(request):
    logout(request)
    return redirect('login')
