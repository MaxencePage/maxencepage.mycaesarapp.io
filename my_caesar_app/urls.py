from django.urls import path
from caesar import views

urlpatterns = [
    path('', views.caesar_view, name='caesar'),
]
