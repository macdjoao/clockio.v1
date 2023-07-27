from django.contrib import admin
from employee.models import Role, Clock


class RoleAdmin(admin.ModelAdmin):
    ...


admin.site.register(Role, RoleAdmin)
