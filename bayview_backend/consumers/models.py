from django.db import models
from safedelete.models import SafeDeleteModel
from bayview.models import AbstractBayView
from safedelete.models import SOFT_DELETE_CASCADE
from business_units.models import BusinessUnit
# Create your models here.


class Consumer(SafeDeleteModel, AbstractBayView):
    """
    ref jira: BWM-92
    """

    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    client_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )
    client_secrte_key = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_consumer = models.BooleanField(default=False)
    business_unit = models.ForeignKey(
        BusinessUnit,
        related_name='business_unit_consumers',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)
