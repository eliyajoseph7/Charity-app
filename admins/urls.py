
from django.contrib import admin
from django.urls import path
from . import views as v

app_name = 'admins'

urlpatterns = [
    path('login', v.login, name='login'),
    path('logout', v.logout_view, name='logout'),
    path('dashboard', v.home_dashboard, name='dashboard'),
    path('user_profile/<int:id>', v.user_profile, name='user_profile'),
    path('update_profile/<int:id>', v.update_profile, name='update_profile'),
    path('users', v.users_view, name='users'),
    path('inbox', v.inbox_view, name='inbox'),
    path('inbox/<slug:slug>', v.email_view, name='read_email'),
    path('update-staff/<int:id>', v.update_staff, name='updateStaff'),
]
