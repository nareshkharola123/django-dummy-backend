from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
#from tenant_schemas.models import TenantMixin
from bayview.models import AbstractBayView

# Create your models here.


class BusinessUnit(SafeDeleteModel, AbstractBayView):
    """
    Jira ref: BWM-91
    """
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    #auto_create_schema = True

    def __str__(self):
        return "#"+str(self.id) + str(self.name)
