from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    bio = models.TextField(_("biography"), max_length=500, blank=True)
    profile_picture = models.ImageField(_("profile picture"), upload_to='media/profile_pictures/', null=True, blank=True)
    

class Post(models.Model):
    media = models.FileField(_("media"), upload_to='media/posts/', null=True, blank=True)
    caption = models.CharField(_("caption"), max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    likes = models.PositiveIntegerField(_("likes"), default=0)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at:%Y-%m-%d}"
