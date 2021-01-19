from django.shortcuts import render
from django.http import HttpResponse


def guestbook(request):
    return HttpResponse("Hello, this is the guestbook form page!")




