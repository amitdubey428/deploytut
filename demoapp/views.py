from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<b>Hello, world. You're at the homepage of your app.</b>")