from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Question, Result

# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def submit_survey(request):
    if request.method == 'POST':
        pass

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def result(request):
    return render(request, 'result.html')