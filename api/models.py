from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_stack = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.student_name

class MoringaMerch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self) -> str:
        return self.name