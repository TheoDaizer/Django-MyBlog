from django.urls import path
from . import views as about_views

urlpatterns = [
    path('', about_views.AboutMeView.as_view(), name='about_me'),
    ]