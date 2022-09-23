from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login


def home_page(request):
    return render(request, 'index.html')


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
            if user is not None:
                login(request, user)
                return redirect('home_page')
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
