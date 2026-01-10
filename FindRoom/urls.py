from django.contrib import admin
from django.urls import path,include
from .views import root

urlpatterns = [
    path("", root),      
    path("admin/", admin.site.urls),
    path("auth/",include('apps.users.urls')),
    path("rooms/",include('apps.rooms.urls')),
]
