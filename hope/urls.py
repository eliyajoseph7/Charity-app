
from django.contrib import admin
from django.urls import path
from . import views as v

app_name = 'hope'

urlpatterns = [
    path('', v.index, name='index'),
    path('about', v.about_view, name='about'),
    path('view/<slug:slug>', v.blog_view, name='view'),
    path('contactMessage', v.contact_view, name='message'),
    path('portfolios', v.portfolio_view, name='portfolios'),
    path('about-me', v.about_me, name='about_me'),
]
