from django.db import models


# write own models here


class AbstractBayView(models.Model):
    """
    this model will be inherit by all the models in
    the project
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
