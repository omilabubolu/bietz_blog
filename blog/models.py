from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
# Test Model
class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def add_note(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title