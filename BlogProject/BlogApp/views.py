from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def basepage(request):
    context = {}
    return render(request,'BlogApp/base.html',context)

def home(request):
    return render(request,'BlogApp/home.html')