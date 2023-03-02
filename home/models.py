from django.db import models
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=now)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=(self.pk, self.title))
