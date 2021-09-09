from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):

    name = models.CharField(
        max_length=40,
        unique=True,
    )

    USERNAME_FIELD = "name"

    def __str__(self):
        return self.name


class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="message", on_delete=models.CASCADE)
    destination_user_id = models.IntegerField()
    message = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Actions(models.Model):
    like = models.BooleanField(default=False, null=True)
    unlike = models.BooleanField(default=False, null=True)
    message_id = models.ForeignKey(
        Message, related_name="like", on_delete=models.CASCADE
    )
