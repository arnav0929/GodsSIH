import email
from email.mime import image
from django.shortcuts import render, HttpResponse, redirect
import sys
from subprocess import run, PIPE
from education import database
import sqlite3
from time import time
import os
conn = sqlite3.connect('godseye.db',check_same_thread=False)
from education.forms import UploadForm
from education import models,usercache
from django.core.files.storage import FileSystemStorage
from education import usercache
from django.http import HttpResponse  


userid=-1
inp=""

def index(request):
    if request.method == 'POST':   
        print(1)
        # conn.execute('''CREATE TABLE subscription 
        #   (subsID INTEGER PRIMARY KEY AUTOINCREMENT,
        #   userID INT NOT NULL,
        #   courseID INT NOT NULL,
        #   location text NOT NULL);''')

        # conn.execute("ALTER TABLE subscription drop column location")     
        run([sys.executable, 'education/intro.py'],
            shell=False, stdout=PIPE)
        run([sys.executable, 'education/main.py'],
            shell=False, stdout=PIPE)
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request,'login.html')



def loginstudent(request):
    if(request.method=='POST'):
        
        email=request.POST.get('email')
        password=request.POST.get('password')
        profile=database.verify_user(email,password)
        print(profile)
        if(profile[0]==-1):
            return HttpResponse("Password or Email Wrong!!")
        else:
            s = "select fname, lname from users where email='" + \
            email+"' and password='"+password+"' "
            print(s)
            cursor = conn.execute(s)
            
            for row in cursor:
                usercache.user.append(str(row[0])+" "+str(row[1]))
            print(usercache.user[len(usercache.user)-1])
            return render(request, 'index.html')
    return render(request, 'loginstudent.html')

def loginmentor(request):
    if(request.method=='POST'):
        email=request.POST.get('email')
        password=request.POST.get('password')
        meet=request.POST.get('meet')
        profile=database.verify_mentor(email,password,meet)
        print(profile)
        if(profile[0]==-1):
            return HttpResponse("Password or Email Wrong!!")
        else:
            # s = "select name from mentor where email='" + \
            # email+"' and password='"+password+"' "
            # cursor = conn.execute(s)
            # context=""
            # for row in cursor:
            #     context=row[0]
            usercache.user.append(meet)
            return render(request, 'mentor.html',{})
    return render(request, 'loginmentor.html')


def register(request):
    return render(request, 'register.html')

def registerstudent(request):
    if(request.method=='POST'):
    #if(role.id=='student'):
        # conn.execute('''CREATE TABLE users
        #         (userID INTEGER PRIMARY KEY AUTOINCREMENT,
        #         fname           TEXT    NOT NULL,
        #         lname            TEXT,
        #         email        TEXT NOT NULL
        #         );''')


        # conn.execute("alter table users add password TEXT")
        # conn.execute("alter table users add mentorID INT")
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conpassword=request.POST.get('conpassword')
        print("Password")
        print(password," ",conpassword)
        if(password!=conpassword):
             return HttpResponse("Password not Match!!")
        else:
             database.add_user(firstname,lastname,email,password)
             return render(request,'login.html')
    return render(request, 'registerstudent.html')

def registermentor(request):
    if(request.method=='POST'):
    #if(role.id=='student'):
        # conn.execute('''CREATE TABLE users
        #         (userID INTEGER PRIMARY KEY AUTOINCREMENT,
        #         fname           TEXT    NOT NULL,
        #         lname            TEXT,
        #         email        TEXT NOT NULL
        #         );''')


        # conn.execute("alter table users add password TEXT")
        # conn.execute("alter table users add mentorID INT")
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conpassword=request.POST.get('conpassword')
        print("Password")
        print(password," ",conpassword)
        if(password!=conpassword):
             return HttpResponse("Password not Match!!")
        else:
             database.add_mentor(name,email,password)
             return render(request,'login.html')
    return render(request, 'registermentor.html')

def forgot(request):
    return render(request, 'forgot.html')


def main_view(request):
    return render(request, 'main.html')

def mentor(request):
    return render(request,'mentor.html',{})

def awareness(request):
    return render(request, 'awareness.html')

def forgot(request):
    return render(request, 'forgot.html')

# def dataadded(request):
#     return render(request, 'dataadded.html')

# def addrelative(request):
#     return render(request,'addrelative.html')
