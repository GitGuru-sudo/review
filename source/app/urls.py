from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    
    path('',views.login,name="login"),
    path('index',views.index,name="index"),
    path('review',views.review,name="review")
]