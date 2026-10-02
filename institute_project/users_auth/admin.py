from django.contrib import admin

# Register your models here.
from users_auth.models import *


admin.site.register(UserModel)
admin.site.register(TeacherModel)