from django.contrib import admin

# Register your models here.
from teachers.models import UserModel, TeacherModel


admin.site.register(TeacherModel)