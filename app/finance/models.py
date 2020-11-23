from django.db import models


class CollectionOrder(models.Model):
    """收款单据"""
    number = models.CharField(max_length=64)
    client = models.CharField(max_length=64)
    create_datetime = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)
    remark = models.CharField(max_length=64, null=True, blank=True)
