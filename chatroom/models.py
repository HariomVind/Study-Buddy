from django.db import models
from user import models as user_model
from user import models as user_model
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.utils.crypto import get_random_string
import random
# Create your models here.

class Room(models.Model):
    rslug = models.SlugField(unique=True, null=True, blank=True)
    rimage = models.ImageField(upload_to="images/", null=True, blank=True)
    ruser = models.ManyToManyField(user_model.User, related_name="ruser", blank=True)
    rname = models.CharField(max_length=100)
    rdescription = models.TextField()
    rcourse = models.ManyToManyField(user_model.Usercourse, related_name="rcourse")
    rcollege = models.ManyToManyField(user_model.Usercollege, related_name="rcollege")
    rcreated_by = models.ForeignKey(user_model.User, on_delete=models.PROTECT, related_name="rcreatedby", blank=True, null=True)
    rcreated_on = models.DateTimeField(auto_now=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.rslug:
            while True:
                new_slug = f"{slugify(self.rname, allow_unicode=True)}-{random.randint(000,999)}-{get_random_string(length=5)}" 
                try:
                    Room.objects.get(rslug=new_slug)
                except :
                    self.rslug=new_slug
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return self.rname

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(user_model.User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)