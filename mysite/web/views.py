from django.shortcuts import render


def hello(request):
    return render(request, 'main.html')


def contacts(request):
    return render(request, 'contacts.html')
