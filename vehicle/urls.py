from django.urls import path
from .views import *

urlpatterns = [
    path('DeviceDetailsView/', DeviceDetailsView.as_view(),  ),
]
