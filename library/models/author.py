from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
