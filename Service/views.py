from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Shortner
from django.db import IntegrityError


def home(request):
    return render(request, 'index.html')


def done(request):
    if request.method == 'POST':
        try:
            data = Shortner()
            website = request.POST['website']
            short_code = request.POST['short-code']
            data.short_code = short_code
            data.website = website
            data.save()
            value = "https://abtohogahi.herokuapp.com/"+data.short_code
            return render(request, 'done.html', {"data": value})
        except IntegrityError:
            return render(request, 'not-found.html', {"message": "The Short Name You Tried is already in Use.\n Please try another one."})
    else:
        return redirect('home')


def route(request, code):
    try:
        data = Shortner.objects.get(short_code=code)
        redirect_link = data.website
        return redirect(redirect_link)
    except Shortner.DoesNotExist:
        return render(request, 'not-found.html', {"message": "The Link you are Trying to Access does not Exists."})
