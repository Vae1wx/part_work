from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['number', 'name', 'contacts',
                  'phone', 'email', 'address', 'remark']

    def create(self, validated_data):
        
        return Supplier.objects.create(**validated_data)

    def update(self, instance, validated_data):
       
        instance.number = validated_data.get('number', instance.number)
        instance.name = validated_data.get(
            'name', instance.name)
        instance.contacts = validated_data.get('contacts', instance.contacts)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.save()
        return instance
