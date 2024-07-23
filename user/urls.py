from django.urls import path
from user import views as user_view

urlpatterns = [
    path('register/', user_view.registeruser, name="register"),
    path('login/', user_view.loginuser, name="login"),
    path('logout/', user_view.logoutuser, name="logout"),
    path('addcollege/', user_view.addcollege, name="addcollege"),
    path('addcourse/', user_view.addcourse, name="addcourse"),
]