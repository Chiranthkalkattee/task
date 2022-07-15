from django.urls import path
from .views import EmployeeList,EmployeeDetails,Department_list

urlpatterns = [
    path('employee/', EmployeeList),
    path('emp_details/<int:pk>/', EmployeeDetails),
    path('department/',Department_list)

]