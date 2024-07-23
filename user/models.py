from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usercourse(models.Model):
    course = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.course


class Usercollege(models.Model):
    college = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.college

class User(AbstractUser):
    ucourse = models.ForeignKey(Usercourse, on_delete=models.PROTECT,null=True, blank=True)
    ucollege = models.ForeignKey(Usercollege, on_delete=models.PROTECT,null=True, blank=True)

    def __str__(self):
        return self.username