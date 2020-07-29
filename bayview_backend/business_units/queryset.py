from django.shortcuts import get_object_or_404
from .models import BusinessUnit


# write query or orm here


class BusinessUnitsQuery:
    """
    this class will be used as abstraction layer between the data access
    layer and business logic layer. it will fetch data from models and
    will pass to service layer
    """
    def __init__(self, value=BusinessUnit):
        self.business_unit = value

    def get_all_business_units(self):
        bussiness = self.business_unit.objects.all()
        return bussiness

    def get_business_unit_object(self, pk):
        business_unit = get_object_or_404(self.business_unit, id=pk)
        return business_unit
