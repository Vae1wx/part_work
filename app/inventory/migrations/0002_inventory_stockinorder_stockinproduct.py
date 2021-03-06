# Generated by Django 2.2.15 on 2020-11-23 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StockInProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.CharField(max_length=32)),
                ('product_specification', models.CharField(max_length=256)),
                ('quantity', models.FloatField()),
                ('product_unit', models.CharField(blank=True, max_length=32, null=True)),
                ('unit_price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_in_product_set', to='basic.Product')),
                ('stock_in_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_in_product_set', to='inventory.StockInOrder')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='basic.Product')),
            ],
        ),
    ]
