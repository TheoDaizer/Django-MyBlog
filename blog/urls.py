from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.BlogView.as_view(), name='blog'),
    path('add_post', blog_views.AddPostView.as_view(), name='add_post'),
    path('<int:pk>', blog_views.DetailPostView.as_view(), name='detail_post_by_id'),
    path('<str:slug>', blog_views.DetailPostView.as_view(), name='detail_post'),
    path('<int:pk>/edit', blog_views.EditPostView.as_view(), name='edit_post_by_id'),
    path('<str:slug>/edit', blog_views.EditPostView.as_view(), name='edit_post'),
    ]