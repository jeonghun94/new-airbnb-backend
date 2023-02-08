from django.contrib import admin
from django.urls import path

from rooms import views as room_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rooms", room_views.say_hello),
]
