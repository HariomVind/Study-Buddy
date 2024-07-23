from django.urls import path
from chatroom import views as chatroom_view
from user import views as user_view

urlpatterns = [
    path('', user_view.home, name="home"),
    path('createroom/', chatroom_view.CreateRoom, name="createroom"),
    path('myroom/', chatroom_view.MyRooms, name="myroom"),
    path('allroom/', chatroom_view.AllRooms, name="allroom"),
    path('search/', chatroom_view.rooomsearch, name="search"),
    path('joinroom/<slug:rslug>/', chatroom_view.joinroom, name="joinroom"),
    path('joinedroom/', chatroom_view.joinedroom, name="joinedroom"),
    path('chat/<slug:rslug>/', chatroom_view.chat, name="chat"),
]