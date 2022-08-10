from django.db import models

class Title(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='Watching', choices=(('Seen', 'Seen'), ('Watching', 'Watching'), ('Planning', 'Planning'), ('Dropped', 'Dropped')))
    poster = models.URLField()

    def __str__(self):
        return self.title