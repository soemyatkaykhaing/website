from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/Index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/Detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre']
    success_url = reverse_lazy('music:index')


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre']
    success_url = reverse_lazy('music:index')


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
