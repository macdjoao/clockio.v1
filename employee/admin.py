from django.contrib import admin
from employee.models import Role, Clock


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    ...


@admin.register(Clock)
class ClockAdmin(admin.ModelAdmin):
    ...
