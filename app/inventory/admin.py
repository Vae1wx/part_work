from django.contrib import admin
from .models import Inventory, StockInOrder, StockInProduct, StockOutOrder, StockOutSquareProduct
# Register your models here.


class InventoryAdmin(admin.ModelAdmin):
	list_display = ['product', 'quantity']
	search_fields = ['product']


class StockInOrderAdmin(admin.ModelAdmin):
	list_display = ['number', 'create_date', 'is_complete']
	search_fields = ['product']


class StockInProductAdmin(admin.ModelAdmin):
	list_display = ['stock_in_order', 'product', 'product_number', 'product_specification', 'quantity',
                 'product_unit', 'unit_price', 'total_amount']
	search_fields = ['stock_in_order']


class StockOutOrderAdmin(admin.ModelAdmin):
	list_display = ['number', 'product_type', 'create_date', 'is_complete']
	search_fields = ['number']


class StockOutSquareProductAdmin(admin.ModelAdmin):
	list_display = [ 'product', 'product_number', 'diameter', 'length', 'quantity',
                 'goods_unit', 'weight', 'caculate_weight', 'unit_price', 'other_fee', 'total_amount', 'remark']
	search_fields = ['stock_out_order']

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(StockInOrder, StockInOrderAdmin)
admin.site.register(StockInProduct, StockInProductAdmin)
admin.site.register(StockOutOrder, StockOutOrderAdmin)
admin.site.register(StockOutSquareProduct, StockOutSquareProductAdmin)
