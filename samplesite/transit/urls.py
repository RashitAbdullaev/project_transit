from django.urls import path,include
from .views import Request_all

urlpatterns = [
    path('', include('allauth.urls')),
    path('', Request_all.as_view(), name='request'),
]
