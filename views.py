from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Employee_details
from .serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])

def EmployeeList(request):

    if request.method == 'GET':
        emp = Employee_details.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])

def EmployeeDetails(request, pk):
    try:
        emp = Employee_details.objects.get(pk=pk)
    except Employee_details.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = EmployeeSerializer(emp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        Employee_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
