from django.urls import path
from employee import views

app_name = 'employees'
# employees-home
# employees-about
# employees-contact

urlpatterns = [
    path('', views.home, name="home"),
    path('about/<int:id>/', views.about, name="about"),
    path('contact/', views.contact, name="contact")
]
