from django.contrib import admin
from . import models as user_model
# Register your models here.

admin.site.register(user_model.User)
admin.site.register(user_model.Usercourse)
admin.site.register(user_model.Usercollege)