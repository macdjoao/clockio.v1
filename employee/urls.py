from django.urls import path
from employee import views

urlpatterns = [
    path('', views.home),
    path('about/<int:id>/', views.about),
    path('contact/', views.contact)
]
