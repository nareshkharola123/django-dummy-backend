from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from django.db import models
from bayview.models import AbstractBayView

# Create your models here.


class Customer(SafeDeleteModel, AbstractBayView):

    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return str(self.customer_id)
