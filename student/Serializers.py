from rest_framework import serializers
from student import models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.course
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):

    #course=serializers.StringRelatedField(read_only=True)
    course=CourseSerializer(read_only=True)
    course_id=serializers.PrimaryKeyRelatedField(
        queryset=models.course.objects.all(),
        source='course',
        write_only=True,
    )

    class Meta:
        model=models.student
        fields=['name','age','course_id','enrolled_on','course']



