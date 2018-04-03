from django.db import models


class Webservicedoc(models.Model):
    wadl_raw = models.TextField()

    def __str__(self):
        return '%s' % (self.wadl_raw)
