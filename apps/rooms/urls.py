from django.urls import path
from apps.rooms.views import CreateRoomView,UpdateRoomView,DeleteRoomView,ProviderRoomDetailView,PublicRoomDetailView,ProviderRoomsView,PublicRoomsView


urlpatterns=[
    path('',PublicRoomsView.as_view(),name="public-rooms"),
    path('<int:pk>/',PublicRoomDetailView.as_view(),name="get-public-room"),
    path('create-room/',CreateRoomView.as_view(),name="create-room"),
    path('get-rooms/',ProviderRoomsView.as_view(),name="get-rooms-by-provider"),
    path('get-room/<int:pk>/',ProviderRoomDetailView.as_view(),name="get-room-by-provider"),
    path('update-room/<int:pk>/',UpdateRoomView.as_view(),name="update-room"),
    path('delete-room/<int:pk>/',DeleteRoomView.as_view(),name="delete-room"),
]