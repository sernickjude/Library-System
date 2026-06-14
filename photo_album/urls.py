from django.urls import path
from . import views

app_name = 'photo_album'

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='album_list'),
    path('create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_edit'),
    path('<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    path('<int:album_pk>/photos/add/', views.PhotoCreateView.as_view(), name='photo_add'),
    path('photos/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
]