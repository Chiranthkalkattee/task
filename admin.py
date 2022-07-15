from django.contrib import admin
from .models import Employee_details, Department_details


# Register your models here.
admin.site.register(Employee_details)
admin.site.register(Department_details)