from django.urls import path
from . import views as projects_views

urlpatterns = [
    path('', projects_views.ProjectsView.as_view(), name='projects'),
    ]