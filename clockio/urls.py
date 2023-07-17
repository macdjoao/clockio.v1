from django.contrib import admin
from django.urls import path
from employee.views import home, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact)
]
