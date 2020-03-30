from django.db import models


class Shortner(models.Model):
    website = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, error_messages={'unique': "This Short Code is Already in use"})
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website
