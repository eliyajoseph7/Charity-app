
from django.contrib import admin
from django.urls import path
from . import views as v

app_name = 'admins'

urlpatterns = [
    path('login', v.login, name='login'),
    path('logout', v.logout_view, name='logout'),
    path('dashboard', v.home_dashboard, name='dashboard'),
    path('user_profile/<int:id>', v.user_profile, name='user_profile'),
]
