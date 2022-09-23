from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name= 'home_page'),
    path('login.html', views.login_user, name = 'login_user'),
   
    path("base.html", views.logout_view, name= "logout"),
    path('register.html', views.register_user, name='register_user'),
    path('profile.html', views.profile),
    path('table.html', views.table),
    path('index.html', views.dashboard),
    path('addCourse.html', views.addCourse),
    path('chat.html', views.chat),
    path('candidates.html', views.candidates),
    path('explore.html', views.explore),
    path('host.html', views.host),
    path('jobs.html', views.jobs),
    path('trackCourse.html', views.trackCourse),
    path('index.html', views.logout_view),
]
