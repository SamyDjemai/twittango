from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth import authenticate, login

from .models import Tweet
from .forms import SignUpForm


def index_view(request):
    return render(request, "core/index.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("feed")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


class TweetListView(ListView):
    model = Tweet
    ordering = ["-created_at"]
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class TweetDetailView(DetailView):
    model = Tweet
    template_name = "core/tweet_detail.html"
