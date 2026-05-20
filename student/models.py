from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

class course(models.Model):
    title=models.CharField(max_length=100)
    duration_month=models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(1)])
    fees=models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
            return self.title

    class Meta:
        ordering=['title']

# Create your models here.
class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,validators=[MaxLengthValidator(100)])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    course = models.ForeignKey('course',on_delete=models.CASCADE,related_name='students',null=True)
    enrolled_on=models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'student'
        ordering = ['id']

