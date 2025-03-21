from django.urls import path
from . import views

urlpatterns = [
    path('', views.rac, name='rac'),

]