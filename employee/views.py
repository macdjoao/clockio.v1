from django.shortcuts import render


def home(request):
    return render(request, 'employee/pages/home.html', context={
        'name': 'João',
        'created_at': ''
    })


def about(request, id: int):
    return render(request, 'employee/pages/about.html')


def contact(request):
    return render(request, 'employee/pages/contact.html')
