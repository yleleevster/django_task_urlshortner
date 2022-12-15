from django.db import models


class ShortURL(models.Model):
    """
    Class for model creation with given parameters.
    """
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100)
    time_date_created = models.DateTimeField()

    def __str__(self):
        return self.original_url
