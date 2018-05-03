from django.contrib import admin
from django.urls import path, re_path
from simplemooc.courses import views

app_name = 'course'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:pk>/', views.details, name='details'),
    path('<slug:slug>/', views.details, name='details'),
]
