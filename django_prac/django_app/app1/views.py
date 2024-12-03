from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Address
# from django_app.app1 import models
from .serializers import StudentSerializer, AddressSerializer
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import permission_classes
# from .throttles import StudentListThrotttle
from rest_framework.throttling import ScopedRateThrottle
class AddressListAV(APIView):

    def get(self, request):
        students = Address.objects.all()
        if students:
            serializer = AddressSerializer(students, many=True)
            return Response(serializer.data)
        return Response(data="No Data")

class MovieListAV(APIView):
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'student-list'
    def get(self, request):
        students = Student.objects.all()
        if students:
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        return Response(data="No Data")

    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()  # While calling save() it will decide whether call create() or update()
            return Response(student.data, status=201)
        return Response(student.errors, status=400)


class SingleMovieAV(APIView):

    def get(self, request, id):
        student = Student.objects.get(pk=id)
        if student:
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=200)

    def put(self, request, id):
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()  ### call the update method
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        student = Student.objects.get(pk=id)
        if student:
            student.delete()
            data = {"message": "student deleted successfully"}
            return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@permission_classes([permissions.IsAdminUser])
def get_student_details(request):
    try:
        if request.method == "GET":
            students = Student.objects.all()
            if students:
                serializer = StudentSerializer(students, many=True)
                return Response(serializer.data)
            return Response(data="No Data")
        if request.method == "POST":
            student = StudentSerializer(data=request.data)
            if student.is_valid():
                student.save()  # While calling save() it will decide whether call create() or update()
                return Response(student.data, status=201)
            return Response(student.errors, status=400)
    except Exception as e:
        print(e)
        return Response(data=e)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def get_single_student(request, pk):
    try:
        if request.method == 'GET':
            student = Student.objects.get(pk=pk)
            if student:
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=200)
        if request.method == 'PUT':
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()       ### call the update method
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        if request.method == 'PATCH':
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()       ### call the update method
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        if request.method == 'DELETE':
            student = Student.objects.get(pk=pk)
            if student:
                student.delete()
                data = {"message": "student deleted successfully"}
                return Response(data, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(e)
        data = {"message": str(e)}
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
