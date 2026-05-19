from rest_framework import serializers
from student.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
            model=student
            fields='__all__'

