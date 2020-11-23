from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name',
                  'phone', 'email', 'permissions', 'remark', 'is_active', 'last_login', 'create_date', 'is_superuser']

    def create(self, validated_data):
        
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
       
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get(
            'name', instance.name)
        
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.permissions = validated_data.get(
            'permissions', instance.permissions)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.last_login = validated_data.get(
            'last_login', instance.last_login)
        instance.create_date = validated_data.get(
            'create_date', instance.create_date)
        instance.is_superuser = validated_data.get(
            'is_superuser', instance.is_superuser)
        instance.save()
        return instance
