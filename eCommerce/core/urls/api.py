from django.urls import path

from ..views.user_api import RegisterUser

urlpatterns = [
    path('users/register/', RegisterUser.as_view())
]
