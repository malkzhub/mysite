from django.urls import path
from . import views

urlpatterns = [
    # app
    path('', views.index, name='index')
]