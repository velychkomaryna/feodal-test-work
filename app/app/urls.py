from django.contrib import admin
from django.urls import path, include
from todo_api import urls as todo_urls
from user import urls as user_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("todo-api/", include(todo_urls)),
    path("users-api/", include(user_urls)),
]
