from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(Person):
    university = models.CharField(max_length=100)

class Worker(Person):
    company = models.CharField(max_length=100)

    class Meta:
        db_table = 'worker'