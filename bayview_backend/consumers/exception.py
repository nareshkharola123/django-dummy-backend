from rest_framework.exceptions import APIException
from consumers.message_exception import (exception_service_not_available,
                                         exception_business_unit_required)

# wrtie custom excption here


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = exception_service_not_available


class BusinessUnitRequired(APIException):
    status_code = 400
    default_detail = exception_business_unit_required
