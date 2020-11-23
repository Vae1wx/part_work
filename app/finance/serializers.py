from rest_framework import serializers
from .models import CollectionOrder


class CollectionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionOrder
        fields = ['number', 'client', 'create_datetime',
                  'amount', 'remark']

    def create(self, validated_data):
        
        return CollectionOrder.objects.create(**validated_data)

    def update(self, instance, validated_data):
       
        instance.number = validated_data.get('number', instance.number)
        instance.client = validated_data.get(
            'client', instance.client)
        instance.create_datetime = validated_data.get(
            'create_datetime', instance.create_datetime)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.remark = validated_data.get(
            'remark', instance.remark)
        instance.save()
        return instance
