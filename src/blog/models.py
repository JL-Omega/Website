from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    author = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'

    def __str__(self):
        return self.title

