from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(blank=True, max_length=255, default='Watching', choices=(('Seen', 'Seen'), ('Watching', 'Watching'), ('Planning', 'Planning'), ('Dropped', 'Dropped')))
    poster = models.URLField(blank=True)
    imdb_URL = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Series(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(blank=True, max_length=255, default='Watching', choices=(('Seen', 'Seen'), ('Watching', 'Watching'), ('Planning', 'Planning'), ('Dropped', 'Dropped')))
    poster = models.URLField(blank=True)
    imdb_URL = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Series\''

    def __str__(self):
        return self.title