from django.contrib import admin
from .models import Supplier, Client, Product, Account
# Register your models here.


class SupplierAdmin(admin.ModelAdmin):
	list_display = ['number', 'name', 'contacts', 'phone', 'email',
                 'address', 'remark', ]
	search_fields = ['number']


class ClientAdmin(admin.ModelAdmin):
	list_display = ['number', 'name', 'level', 'contacts', 'phone', 'email',
                 'address', 'remark', ]
	search_fields = ['number']


class ProductAdmin(admin.ModelAdmin):
	list_display = ['number', 'name', 'unit', 'purchase_price', 'sales_price']
	search_fields = ['number']


class AccountAdmin(admin.ModelAdmin):
	list_display = ['number', 'name', 'remark', 'is_active']
	search_fields = ['number']

admin.site.register(Supplier, SupplierAdmin) 
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Account, AccountAdmin)
