from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    display_name = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        help_text="The main name displayed on your profile.",
    )
    bio = models.TextField(
        max_length=100, default="", null=False, help_text="Describe yourself!"
    )


class Tweet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=140, blank=False, null=False,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user}: {self.text}"

    def get_absolute_url(self):
        return reverse("tweet_detail", kwargs={"pk": self.pk})
