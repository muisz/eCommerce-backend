from django.urls import path

from ..views.user_api import RegisterUser, GetStore
from ..views.product_api import ItemView

urlpatterns = [
    # user
    path('users/register/', RegisterUser.as_view()),
    # stores
    path('stores/', GetStore.as_view()),
    # item
    path('items/', ItemView.as_view())
]
