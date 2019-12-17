from django.urls import path
from . import views
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]