from django.urls import path
from .views import EmployeeList,EmployeeDetails

urlpatterns = [
    path('employee/', EmployeeList),
    path('emp_details/<int:pk>/', EmployeeDetails)

]