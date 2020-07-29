from rest_framework.exceptions import APIException
from business_units.message_exception import exception_service_not_available

# wrtie custom excption here


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = exception_service_not_available
