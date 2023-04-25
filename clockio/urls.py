from django.urls import path
from clockio.views import index

urlpatterns = [
    path('', index)
]
