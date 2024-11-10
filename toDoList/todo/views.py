from django.shortcuts import render


def index(request):
    return render(request, 'todo/index.html')


def about(request):
    return render(request, 'todo/about.html')


def auth(request):
    return render(request, 'acc/auth.html')