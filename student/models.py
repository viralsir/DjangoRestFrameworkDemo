from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,validators=[MaxLengthValidator(100)])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])


    def __str__(self):
        return self.name
    class Meta:
        db_table = 'student'
        ordering = ['id']

