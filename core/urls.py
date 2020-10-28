from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index_view, signup, TweetListView, TweetDetailView

urlpatterns = [
    path("", index_view, name="index"),
    path("feed", TweetListView.as_view(), name="feed"),
    path("tweet/<int:pk>", TweetDetailView.as_view(), name="tweet_detail"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("signup", signup, name="signup"),
]
