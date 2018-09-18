from django.views import generic
from django.views.generic import CreateView

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
