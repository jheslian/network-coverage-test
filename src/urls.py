from django.urls import path
from .views import NetworkMobileListView

urlpatterns = [
    path('', NetworkMobileListView.as_view(), name='networks'),
]
