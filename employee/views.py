from django.shortcuts import render
from faker import Faker

fake = Faker()


def home(request):
    return render(request, 'employee/pages/home.html', context={
        'id': fake.random_number(digits=2),
        'name': fake.first_name(),
        'created_at': fake.date_time()
    })


def about(request, id: int):
    return render(request, 'employee/pages/about.html')


def contact(request):
    return render(request, 'employee/pages/contact.html')
