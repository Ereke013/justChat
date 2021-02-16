from django.contrib.auth.models import User
from django.db import models

class Group(models.Model):
    name = models.CharField("Group name", max_length=100)


# class User(models.Model):
#     name = models.CharField("full name", max_length=50)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     user_ava = models.CharField("User Photo ", max_length= 250)
#     # group_id = models.IntegerField()

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField
    message_text = models.TextField("Message text")



