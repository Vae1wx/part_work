from django.contrib import admin
from .models import CollectionOrder
# Register your models here.


class CollectionOrderAdmin(admin.ModelAdmin):
	list_display = ['number', 'client', 'create_datetime', 'amount', 'remark']
	search_fields = ['number']


admin.site.register(CollectionOrder, CollectionOrderAdmin)
