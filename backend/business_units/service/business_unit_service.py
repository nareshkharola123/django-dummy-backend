from ..queryset import BusinessUnitsQuery
from business_units.message_exception import exception_business_unit_service_name  # NOQA
from business_units.exception import ServiceUnavailable

# write main business logic here


class BusinessUnitService:
    """
    here we will write our all busines-logic and
    get data from queryset and return views
    """

    def __init__(self, value=BusinessUnitsQuery):
        self.business_unit_query = value()

    def business_unit_all(self):
        try:
            bussiness_units = self.business_unit_query.get_all_business_units()
            return bussiness_units
        except Exception:
            raise ServiceUnavailable

    def delete_business_unit_object(self, pk):
        bussiness_unit = self.business_unit_query.get_business_unit_object(pk)
        bussiness_unit_dict = {'id': bussiness_unit.id, 'name': bussiness_unit.name}  # NOQA
        try:
            bussiness_unit.delete()
            bussiness_unit_dict['message'] = 'Deleted'
        except Exception as e:
            bussiness_unit_dict['message'] = e
        return bussiness_unit_dict

    def get_business_unit_object(self, pk):
        bussiness_unit = self.business_unit_query.get_business_unit_object(pk)
        return bussiness_unit

    def check_update_business_unit_object(self, pk, data):
        bussiness_unit = self.business_unit_query.get_business_unit_object(pk)
        bussiness_unit_dict = {'id': bussiness_unit.id, 'name': bussiness_unit.name}  # NOQA
        if bussiness_unit.name.lower() == data['name'].lower():
            bussiness_unit.description = data['description']
            bussiness_unit.save()
            bussiness_unit_dict['description'] = bussiness_unit.description
            bussiness_unit_dict['message'] = "updated"
            return bussiness_unit_dict
        else:
            return {"message": exception_business_unit_service_name}
