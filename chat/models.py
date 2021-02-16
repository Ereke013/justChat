from django.contrib.auth.models import User
from django.db import models

class Group(models.Model):
    name = models.CharField("Group name", max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    message_text = models.TextField("Message text")

    def __str__(self):
        return self.message_text


# class Person(models.Model):
#     user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
#     name = models.CharField("full name", max_length=50, null=True, blank=True)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
#     user_ava = models.CharField("User Photo", max_length= 250, null=True, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name = 'пользователь'
#         verbose_name_plural = 'пользователи'
