from django.contrib import admin
from chatroom import models as chatroom_model
# Register your models here.


admin.site.register(chatroom_model.Room)
admin.site.register(chatroom_model.Message)