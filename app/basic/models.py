from django.db import models


class Supplier(models.Model):
    """供应商"""
    number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    contacts = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=256, null=True, blank=True)


class Level(models.Model):
    """客户分级"""
    level = models.CharField(max_length=64)


class Client(models.Model):
    """客户"""
    number = models.CharField(max_length=32)
    name = models.CharField(max_length=64, null=True, blank=True)
    level = models.ForeignKey(
        'basic.Level', models.CASCADE, related_name='client_set')
    contacts = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=256, null=True, blank=True)


class PriceEntry(models.Model):
    """价格条目"""


class Price(models.Model):
    """价格"""
    price_entry = models.ForeignKey(
        'basic.PriceEntry', models.CASCADE, related_name='price_set')


class Product(models.Model):
    """钢材"""
    number = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    unit = models.CharField(max_length=16, null=True, blank=True)  # 单位
    purchase_price = models.FloatField(default=0)
    sales_price = models.FloatField(default=0)  # 售价

    def __str__(self):
        return self.name
    


class Account(models.Model):
    """结算账户"""
    number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    remark = models.CharField(max_length=256, null=True, blank=True)
    is_active = models.BooleanField(default=True)
