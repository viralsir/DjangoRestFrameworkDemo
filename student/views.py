from django.shortcuts import render
from rest_framework import viewsets

from .Serializers import StudentSerializer
from .models import *

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


