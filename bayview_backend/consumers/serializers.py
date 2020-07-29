from rest_framework import serializers
from consumers.models import Consumer

# serializers start here


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'name', 'description', 'client_id', 'client_secrte_key', 'is_active', 'is_consumer', 'business_unit')
