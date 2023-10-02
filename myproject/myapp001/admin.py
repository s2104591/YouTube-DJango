from django.contrib import admin
from .models import Student  # mariano


# Register your models here.
admin.site.register(Student)  #mariano

# after a model change ie database change:
# python manage.py makemigrations
# python manage.py migrate


