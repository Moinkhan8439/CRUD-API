from django.shortcuts import render
from rest_framework import serializers
from accounts.models import student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    url_list={
        'list':'/student-list/',
        'detail view':'/student-detail/<str:pk>',
        'Create':'/add-student/',
        'update':'/update-student/<str:pk>',
        'delete':'/delete-student/<str:pk>',
    }
    return Response(url_list)
        

@api_view(['GET'])
def student_list(request):
    students=student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def student_detail(request,pk):
    students=student.objects.get(id=pk)
    serializer=StudentSerializer(students,many=False)
    return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def add_student(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update_student(request,pk):
    students=student.objects.get(id=pk)
    serializer=StudentSerializer(instance=students,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_student(request,pk):
    students=student.objects.get(id=pk)
    students.delete()
    return Response("student deleted successfully !!")