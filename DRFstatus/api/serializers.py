from rest_framework import serializers
from .models import Order,Status,Workers,TitleJob

class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class Statusserializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class Workersserializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'

class TitleJobserializer(serializers.ModelSerializer):
    class Meta:
        model = TitleJob
        fields = '__all__'


