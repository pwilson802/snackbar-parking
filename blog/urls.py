from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostListViewCategory


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('story/', PostListViewCategory.as_view(), name='story'),
    path('review/', PostListViewCategory.as_view(), name='review'),
    path('category/', PostListViewCategory.as_view(), name='categories'),
]