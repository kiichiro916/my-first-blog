from django.urls import path
from . import views

urlpatterns = [
    path('getall', views.get_all_operation_schedule, name='get_all_operation_schedule'),
]
