from django.db import models

# Create your models here.


#mariano added this class
class Student(models.Model):
    name=models.CharField(max_length=200)
    pass 


# after a model change ie database change:
# python manage.py makemigrations
# python manage.py migrate


# python manage.py createsuperuser
