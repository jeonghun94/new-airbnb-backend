from django.contrib import admin
from django.urls import path, include

from rooms import views as room_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
]
