from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Album, Photo

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'photo_album/album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'photo_album/album_detail.html'
    context_object_name = 'album'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'photo_album/album_form.html'
    success_url = reverse_lazy('photo_album:album_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'photo_album/album_form.html'
    success_url = reverse_lazy('photo_album:album_list')

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

    def test_func(self):
        album = self.get_object()
        return album.owner == self.request.user

class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'photo_album/album_confirm_delete.html'
    success_url = reverse_lazy('photo_album:album_list')

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

    def test_func(self):
        album = self.get_object()
        return album.owner == self.request.user

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'description', 'image']
    template_name = 'photo_album/photo_form.html'

    def form_valid(self, form):
        album = Album.objects.get(pk=self.kwargs['album_pk'], owner=self.request.user)
        form.instance.album = album
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('photo_album:album_detail', kwargs={'pk': self.kwargs['album_pk']})

class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'photo_album/photo_confirm_delete.html'

    def get_queryset(self):
        return Photo.objects.filter(album__owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('photo_album:album_detail', kwargs={'pk': self.object.album.pk})

    def test_func(self):
        photo = self.get_object()
        return photo.album.owner == self.request.user
