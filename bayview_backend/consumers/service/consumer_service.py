import secrets
from consumers.queryset import ConsumerQuery
from consumers.exception import ServiceUnavailable

# write main business logic here


class ConsumerService:

    def __init__(self, value=ConsumerQuery):
        self.consumer_query = value()

    def consumer_all(self):
        try:
            consumers = self.consumer_query.get_all_consumers()
            return consumers
        except Exception:
            raise ServiceUnavailable

    def consumer_add_client_and_secret_key(self, data):
        consumer = self.consumer_query.get_consumer_object(data['id'])
        consumer_name = data['name']
        consumer.client_id = consumer_name.replace(' ', '_')
        consumer.client_secrte_key = secrets.token_hex(20)
        consumer.is_consumer = True
        consumer.save()
        return consumer

    def consumer_deactive(self, pk):
        consumer = self.consumer_query.get_consumer_object(pk)
        consumer.is_active = False
        consumer.save()
        return {'id': consumer.id}
