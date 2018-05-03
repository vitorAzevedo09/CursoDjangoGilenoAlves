from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from simplemooc.accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('sair/', auth_views.logout, {'next_page': 'core:home'}, name='logout'),
    path('cadastre-se/', views.register, name='register'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
    path('nova-senha/', views.password_reset, name='password_reset'),


]
