from django.db import models
from users_auth.models import BasicInfoModel, UserModel


class TeacherModel(BasicInfoModel):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='teacher_profile',
        null=True
    )
    teacher_id = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='media/teacher_img', null=True)

    def __str__(self):
        return f'{self.user.username}'