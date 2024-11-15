from django.db import models

class Joke(models.Model):
    category = models.CharField(max_length=100)
    joke_type = models.CharField(max_length=50)
    joke = models.TextField(null=True, blank=True)  # For 'single' joke type
    setup = models.TextField(null=True, blank=True)  # For 'twopart' joke type
    delivery = models.TextField(null=True, blank=True)  # For 'twopart' joke type
    nsfw = models.BooleanField(default=False)
    political = models.BooleanField(default=False)
    sexist = models.BooleanField(default=False)
    safe = models.BooleanField(default=True)
    lang = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.joke if self.joke else self.setup
