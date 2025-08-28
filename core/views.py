from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def landing(request):
    return render(request, 'landing.html')

