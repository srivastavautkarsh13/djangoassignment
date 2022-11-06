from django.urls import path, include
from .views import CustomeUserCreate

urlpatterns = [
    path('register/', CustomeUserCreate.as_view(), name='create_user')
]
