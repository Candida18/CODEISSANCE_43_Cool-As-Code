from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def home_page(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'index.html')


def login_user(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None and user.is_learner:
                login(request, user)
                return redirect('profile.html')
            elif user is not None and user.is_course:
                login(request, user)
                return redirect('trackCourse.html')
            elif user is not None and user.is_recruiter:
                login(request, user)
                return redirect('candidates.html')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login_user.html', {'form': form, 'msg': msg})


def register_user(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_user')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register_user.html', {'form': form, 'msg': msg})


def profile(request):
    return render(request, 'profile.html')


def table(request):
    return render(request, 'table.html')


def addCourse(request):
    return render(request, 'addCourse.html')


def chat(request):
    return render(request, 'chat.html')


def candidates(request):
    return render(request, 'candidates.html')


def explore(request):
    return render(request, 'explore.html')


def host(request):
    return render(request, 'host.html')


def jobs(request):
    return render(request, 'jobs.html')


def trackCourse(request):
    
    return render(request, 'trackCourse.html')


def logout_view(request):
    logout(request)
    return redirect('home.html')
