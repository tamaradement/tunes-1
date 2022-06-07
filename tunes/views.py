from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Tune, Setlist
from .filters import TuneFilter


class TuneListView(ListView):
    model = Tune
    template_name = "tune_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = TuneFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TuneDetailView(DetailView):
    model = Tune
    template_name = "tune_detail.html"


class TuneUpdateView(UpdateView):
    model = Tune
    fields = (
        "title",
        "composer",
        "key",
        "notes",
        "genre",
        "pdf",
    )
    template_name = "tune_edit.html"


class TuneDeleteView(DeleteView):
    model = Tune
    template_name = "tune_delete.html"
    success_url = reverse_lazy("tune_list")


class TuneCreateView(CreateView):
    model = Tune
    template_name = "tune_new.html"
    fields = (
        "title",
        "composer",
        "key",
        "notes",
        "genre",
        "pdf",
        "performer",
    )


# ==========
# Setlists
# ==========


class SetlistCollection(ListView):
    model = Setlist
    template_name = "setlist_collection.html"


class SetlistDetailView(DetailView):
    model = Setlist
    template_name = "setlist_detail.html"


class SetlistUpdateView(UpdateView):
    model = Setlist
    fields = (
        "title",
        "description",
        "tunes",
    )
    template_name = "setlist_edit.html"


class SetlistDeleteView(DeleteView):
    model = Setlist
    template_name = "setlist_delete.html"
    success_url = reverse_lazy("setlist_collection")


class SetlistCreateView(CreateView):
    model = Setlist
    template_name = "setlist_new.html"
    fields = (
        "title",
        "performer",
        "description",
        "tunes",
    )
