from django.urls import path
from apps.users.views import RegisterView,LoginView,ProfileView,UpdateRoleView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns=[
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('refresh/',TokenRefreshView.as_view(),name="token-refresh"),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('update-role/',UpdateRoleView.as_view(),name="update-role"),
]