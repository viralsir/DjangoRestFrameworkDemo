from django.shortcuts import render
from rest_framework import viewsets

from .Serializers import StudentSerializer, CourseSerializer
from .models import *

class CourseViewSet(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = CourseSerializer



# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    '''
     post
     get
     put
     patch
     delete
    '''
    queryset = student.objects.all()
    serializer_class = StudentSerializer


