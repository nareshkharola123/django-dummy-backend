from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from django.db import models
from bayview.models import AbstractBayView


# Create your models here.


class Template(SafeDeleteModel, AbstractBayView):
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)
    external_template_id = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.name)
