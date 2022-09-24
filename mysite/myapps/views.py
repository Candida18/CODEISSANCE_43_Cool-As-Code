from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, AddCourse
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
from django.http import HttpResponse

import json as simplejson

from django.middleware.csrf import CsrfViewMiddleware
from django.views.decorators.csrf import csrf_exempt

# from django_remote_forms.forms import RemoteForm
from myapps.forms import AddCourse



def home_page(request):
    return render(request, "home.html")


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "index.html")


def login_user(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None and user.is_learner:
                login(request, user)
                return redirect("profile.html")
            elif user is not None and user.is_course:
                login(request, user)
                return redirect("trackCourse.html")
            elif user is not None and user.is_recruiter:
                login(request, user)
                return redirect("candidates.html")
            else:
                msg = "invalid credentials"
        else:
            msg = "error validating form"
    return render(request, "login_user.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = "user created"
            return redirect("login_user")
        else:
            msg = "form is not valid"
    else:
        form = SignUpForm()
    return render(request, "register_user.html", {"form": form, "msg": msg})


def trackCourse(request):
    return render(request, "trackCourse.html")


def profile(request):
    return render(request, "profile.html")


def table(request):
    return render(request, "table.html")


def addCourse(request):


    # if request.method == "POST":
    #     form = AddCourse(request.POST)
    #     # if form.is_valid():

    #     #return redirect("trackCourse.html")
    #     render(request, "addCourse.html", {"form": form})
    # else:
    #     form = AddCourse()
    # return render(request, "addCourse.html", {"form": form})

    # # form = AddCourse(request.POST)
    # # if request.method == 'POST':
    #     # form = AddCourse(request.POST)
    #     # if form.is_valid():
    #         # course = form.save()

    # if request.method == 'POST':
    #     # form = AddCourse(request.POST)
    #     # if form.is_valid():

    #     return redirect('trackCourse.html')
    # else:
    #     form = AddCourse()
    # return render(request, 'addCourse.html', {'form': form})

    # csrf_middleware = CsrfViewMiddleware()

    # response_data = {}
    # if request.method == 'GET':
    #     # Get form definition
    #     form = AddCourse()
    # elif request.raw_post_data:
    #     request.POST = json.loads(request.raw_post_data)
    #     # Process request for CSRF
    #     csrf_middleware.process_view(request, None, None, None)
    #     form_data = request.POST.get('data', {})
    #     form = AddCourse(form_data)
    #     if form.is_valid():
    #         form.save()

    # remote_form = RemoteForm(form)
    # # Errors in response_data['non_field_errors'] and response_data['errors']
    # response_data.update(remote_form.as_dict())
    # data["test1"].append(response_data)
    # response = HttpResponse(
    #     json.dumps(data, cls=DjangoJSONEncoder),
    #     mimetype="application/json"
    # )



    # # Process response for CSRF
    # csrf_middleware.process_response(request, response)
    # return response
   



    
    if request.method == 'POST':
        # form = AddCourse(request.POST)
        # if form.is_valid():

        return redirect('trackCourse.html')
    else:
        form = AddCourse()
    return render(request, 'addCourse.html', {'form': form})

   




def chat(request):
    return render(request, "chat.html")


def candidates(request):
    return render(request, "candidates.html")

def resume(request):
    return render(request, "resume.html")



#WE NEED TO CONSTANTLY CHANGE PATH FOR ALL COMPUTERS



#f = open(r"C:\Users\Lenovo\Documents\GitHub\CODEISSANCE_43_Cool-As-Code\mysite\myapps\dataset\data.json")


f = open(r"C:\Users\noron\CODEISSANCE_43_Cool-As-Code\mysite\myapps\dataset\data.json")

# f = open(r"C:\Users\Sachi\Documents\GitHub\CODEISSANCE_43_Cool-As-Code\mysite\myapps\dataset\data.json")




data = json.load(f)


def explore(request):

    # for i in data['test1']:
    #     print(i)

    # # # Closing file
    # # f.close()

    # print(data)

    return render(request, "explore.html", data)


def courseContent(request):
    # f = open(
    #     r'C:\Users\noron\CODEISSANCE_43_Cool-As-Code\mysite\myapps\dataset\data.json')
    # data = json.load(f)
    return render(request, "courseContent.html", data)


def host(request):
    return render(request, "host.html")


def jobs(request):
    return render(request, "jobs.html")


def logout_view(request):
    logout(request)
    return redirect("home.html")
