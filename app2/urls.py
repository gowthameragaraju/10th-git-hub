from django.urls import path
from app2.views import *
app_name='gowtham_01'
urlpatterns=[
    path("gowtham1/",gowtham1,name='gowtham1'),
]