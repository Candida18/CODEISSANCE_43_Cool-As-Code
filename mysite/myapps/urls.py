from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name= 'home_page'),
    path('login.html', views.login_user, name = 'login_user'),
    path('register.html', views.register_user, name='register_user'),
    path('profile.html', views.profile),
    path('table.html', views.table),
    path('index.html', views.dashboard),
]
