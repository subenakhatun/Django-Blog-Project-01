from django.urls import path
from django.shortcuts import render

# home html er jonno function create kore request set kora
def home(request):
    return render(request,'home.html')