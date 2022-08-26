from django.contrib import admin
from django.urls import path, include
from education.views import *

urlpatterns = [
    path('', home, name='home'),
    path('home.html', home, name='home'),
    path('index.html', index, name='index'),
    path('login.html', login, name='login'),
    path('loginstudent.html', loginstudent, name='loginstudent'),
    path('loginmentor.html', loginmentor, name='loginmentor'),
    path('register.html', register, name='register'),
    path('mentor.html', mentor, name='mentor'),
    path('registerstudent.html', registerstudent, name='registerstudent'),
    path('registermentor.html', registermentor, name='registerstudent'),
    path('forgot.html', forgot, name='forgot'),
    path('awareness.html', awareness, name='awareness'),
]
