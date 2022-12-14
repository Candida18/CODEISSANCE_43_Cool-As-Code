from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name= 'home_page'),
    path('login.html', views.login_user, name = 'login_user'),
    path('applicants.html', views.applicants, ),
    # path('home.html', views.home, name= 'home'),
    path("base.html", views.logout_view, name= "logout"),
    path('register.html', views.register_user, name='register_user'),
    path("courseContent.html", views.courseContent, name= "content"),
    path('profile.html', views.profile),
    path('table.html', views.table),
    path('index.html', views.dashboard),
    path('addCourse.html', views.addCourse),
    path('chat.html', views.chat),
    path('employees.html', views.employees),
    path('explore.html', views.explore,name="explore"),
    path('host.html', views.host),
    path('jobs.html', views.jobs),
    path('trackCourse.html', views.trackCourse),
    path('index.html', views.logout_view),
    path('resume.html', views.resume),
    path('feedback.html', views.feedback),



]
