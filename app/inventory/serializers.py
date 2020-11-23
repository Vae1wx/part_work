from rest_framework import serializers
from .models import Inventory, StockInOrder, StockInProduct, StockOutOrder, StockOutSquareProduct


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity']

    def create(self, validated_data):
        
        return Inventory.objects.create(**validated_data)

    def update(self, instance, validated_data):
       
        instance.product = validated_data.get('product', instance.product)
        instance.quantity = validated_data.get(
            'quantity', instance.quantity)
        
        instance.save()
        return instance


class StockInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInOrder
        fields = ['number', 'create_date', 'is_complete']

    def create(self, validated_data):

        return StockInOrder.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.number = validated_data.get('number', instance.number)
        instance.create_date = validated_data.get(
            'create_date', instance.create_date)
        instance.is_complete = validated_data.get(
            'is_complete', instance.is_complete)
        
        instance.save()
        return instance


class StockInProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInProduct
        fields = ['stock_in_order', 'product', 'product_number',
                  'product_specification', 'quantity', 'product_unit', 'unit_price', 'total_amount']

    def create(self, validated_data):

        return StockInProduct.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.stock_in_order = validated_data.get(
            'stock_in_order', instance.stock_in_order)
        instance.product = validated_data.get(
            'product', instance.product)
        instance.product_number = validated_data.get(
            'product_number', instance.product_number)
        instance.product_specification = validated_data.get(
            'product_specification', instance.product_specification)
        instance.quantity = validated_data.get(
            'quantity', instance.quantity)
        instance.product_unit = validated_data.get(
            'product_unit', instance.product_unit)
        instance.unit_price = validated_data.get(
            'unit_price', instance.unit_price)
        instance.total_amount = validated_data.get(
            'total_amount', instance.total_amount)
        instance.save()
        return instance


class StockOutOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOutOrder
        fields = ['number', 'create_date', 'product_type', 'is_complete']

    def create(self, validated_data):

        return StockOutOrder.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.number = validated_data.get('number', instance.number)
        instance.create_date = validated_data.get(
            'create_date', instance.create_date)
        instance.product_type = validated_data.get(
            'product_type', instance.product_type)
        instance.is_complete = validated_data.get(
            'is_complete', instance.is_complete)

        instance.save()
        return instance


class StockOutSquareProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOutSquareProduct
        fields = ['stock_out_order', 'product',
                  'product_number', 'diameter', 'length', 'quantity', 'goods_unit', 'weight', 
                  'caculate_weight', 'unit_price', 'other_fee', 'total_amount', 'remark']

    def create(self, validated_data):

        return StockOutSquareProduct.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.stock_out_order = validated_data.get(
            'stock_out_order', instance.stock_out_order)
        instance.product = validated_data.get(
            'product', instance.product)
        instance.product_number = validated_data.get(
            'product_number', instance.product_number)
        instance.diameter = validated_data.get(
            'diameter', instance.diameter)
        instance.length = validated_data.get(
            'length', instance.length)
        instance.quantity = validated_data.get(
            'quantity', instance.quantity)
        instance.goods_unit = validated_data.get(
            'goods_unit', instance.goods_unit)
        instance.weight = validated_data.get(
            'weight', instance.weight)
        instance.caculate_weight = validated_data.get(
            'caculate_weight', instance.caculate_weight)
        instance.unit_price = validated_data.get(
            'unit_price', instance.unit_price)
        instance.other_fee = validated_data.get(
            'other_fee', instance.other_fee)
        instance.total_amount = validated_data.get(
            'total_amount', instance.total_amount)
        instance.remark = validated_data.get(
            'remark', instance.remark)

        instance.save()
        return instance
