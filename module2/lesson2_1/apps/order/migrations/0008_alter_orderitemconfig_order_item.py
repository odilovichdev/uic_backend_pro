# Generated by Django 4.2.23 on 2025-07-09 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_orderitemconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemconfig',
            name='order_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='order.orderitem'),
        ),
    ]
