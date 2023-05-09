from django.shortcuts import render
from clockio.models import User


def index(request):
    users = User.objects.all()
    return render(request, 'clockio/index.html', {'users': users})
