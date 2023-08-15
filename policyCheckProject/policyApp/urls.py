from django.urls import path
from . import views

urlpatterns = [
    path('',views.createData, name='create'),
    path('success',views.successpage,name='success')
]
