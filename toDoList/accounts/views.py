from django.shortcuts import render


def auth(request):
    return render(request, 'acc/auth.html')
