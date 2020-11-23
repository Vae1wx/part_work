from django.db import models
from app.basic.models import Product

class Inventory(models.Model):
    """库存"""
    product = models.ForeignKey(
        'basic.Product', models.CASCADE, related_name='inventories')
    quantity = models.FloatField(default=0)


class StockInOrder(models.Model):
    """入库单据"""
    number = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)


class StockInProduct(models.Model):
    """入库钢材"""
    stock_in_order = models.ForeignKey(
        'inventory.StockInOrder', models.CASCADE, related_name='stock_in_product_set')
    product = models.ForeignKey(
        'basic.Product', models.SET_NULL, related_name='stock_in_product_set', null=True)
    product_number = models.CharField(max_length=32)
    product_specification = models.CharField(max_length=256)
    quantity = models.FloatField()
    product_unit = models.CharField(max_length=32, null=True, blank=True)
    unit_price = models.FloatField()
    total_amount = models.FloatField()


    

class StockOutOrder(models.Model):
    """出库单据"""
    number = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    product_type = models.CharField(
        max_length=12, default='round', choices=(('round', '圆钢'), ('square', '方钢')))
    is_complete = models.BooleanField(default=False)


# class StockOutRoundProduct(models.Model):
#     """出库圆钢"""
#     rstock_out_order = models.ForeignKey(
#         'inventory.StockOutOrder', models.CASCADE, related_name='stock_out_product_set')
    # product = models.ForeignKey(
    #     'basic.Product', models.SET_NULL, related_name='stock_out_product_set', null=True)
    # product_number = models.CharField(max_length=32)
    # diameter = models.FloatField()
    # length = models.FloatField()
    # quantity = models.FloatField()
    # goods_unit = models.CharField(max_length=32, null=True, blank=True)
    # weight = models.FloatField()
    # caculate_weight = models.FloatField()
    # unit_price = models.FloatField()
    # other_fee = models.FloatField()
    # total_amount = models.FloatField()
    # remark = models.CharField(max_length=256, null=True, blank=True)


class StockOutSquareProduct(models.Model):
    """出库方钢"""
    stock_out_order = models.ForeignKey(
        'inventory.StockOutOrder', models.CASCADE, related_name='stock_out_product_set')
    product = models.ForeignKey(
        'basic.Product', models.SET_NULL, related_name='stock_out_product_set', null=True)
    product_number = models.CharField(max_length=32)
    diameter = models.FloatField()
    length = models.FloatField()
    quantity = models.FloatField()
    goods_unit = models.CharField(max_length=32, null=True, blank=True)
    weight = models.FloatField()
    caculate_weight = models.FloatField()
    unit_price = models.FloatField()
    other_fee = models.FloatField()
    total_amount = models.FloatField()
    remark = models.CharField(max_length=256, null=True, blank=True)
    
    
    
