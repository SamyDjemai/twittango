from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required

from .models import Tweet
from .forms import SignUpForm, TweetForm


def index_view(request):
    return render(request, "core/index.html")


def profile_view(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    tweets = Tweet.objects.filter(user=user)
    return render(request, "core/profile.html", {"user": user, "tweets": tweets})


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


@login_required
def post_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
    return redirect("feed")


class TweetListView(ListView):
    model = Tweet
    ordering = ["-created_at"]
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context["form"] = TweetForm()
        return context


class TweetDetailView(DetailView):
    model = Tweet
    template_name = "core/tweet_detail.html"
