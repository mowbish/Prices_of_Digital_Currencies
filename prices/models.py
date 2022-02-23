from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class FileDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
