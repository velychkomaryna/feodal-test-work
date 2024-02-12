from django.urls import path
from rest_framework.authtoken import views
from .views import UserRegistrationView, UserLoginView


urlpatterns = [
    path("register", UserRegistrationView.as_view(), name="api-register"),
    path("token/login", UserLoginView.as_view(), name="api-token-login"),
    path("api-token-auth/", views.obtain_auth_token),
]
