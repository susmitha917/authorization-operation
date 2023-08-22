from django.contrib import admin

from django.urls import path,include

from . import views


urlpatterns = [

 path('sign_up/', views.sign_up),

 
]