from rest_framework import serializers
from .models import BusinessUnit
from .message_exception import (exception_business_unit_name,
                                exception_business_unit_validate)

# serializers start here


class BusinessUnitSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        validate the name of business-unit
        """
        try:
            value = data['name']
        except KeyError:
            raise serializers.ValidationError(exception_business_unit_name)
        try:
            if isinstance(eval(value[0]), int):
                raise serializers.ValidationError(exception_business_unit_validate)  # NOQA
        except NameError:
            pass

        #data['schema_name'] = value.replace(' ', '_')
        #data['domain_url'] = 'http:%s.bayview.com' % data['schema_name']
        return data

    def create(self, validated_data):
        data = BusinessUnit.objects.create(**validated_data)
        return data

    class Meta:
        model = BusinessUnit
        fields = ('id', 'name', 'description') # NOQA
