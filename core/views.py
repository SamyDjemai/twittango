from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Tweet


def index_view(request):
    return render(request, "core/index.html")


class TweetListView(ListView):
    model = Tweet
    ordering = ["-created_at"]
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
