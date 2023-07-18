from django.shortcuts import render


def home(request):
    return render(request, 'employee/pages/home.html')


def about(request):
    return render(request, 'employee/pages/about.html')


def contact(request):
    return render(request, 'employee/pages/contact.html')
