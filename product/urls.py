from django.urls import path
from product.views import index, testform, username
from . import views

app_name = "product"

urlpatterns = [
    path("", index, name="index"),
    path("testform/", views.testform, name='testform'),
    path("username/", views.username, name='username'),
   
   

   
]