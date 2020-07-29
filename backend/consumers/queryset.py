from django.shortcuts import get_object_or_404
from consumers.models import Consumer


# write query or orm here


class ConsumerQuery:

    def __init__(self, value=Consumer):
        self.consumer = value

    def get_all_consumers(self):
        consumers = self.consumer.objects.all()
        return consumers

    def get_consumer_object(self, pk):
        consumer = get_object_or_404(self.consumer, id=pk)
        return consumer
