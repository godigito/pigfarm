# Generated by Django 5.1.6 on 2025-04-19 14:41

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0010_alter_feedstock_cost_per_unit_alter_feedstock_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedstock',
            name='initial_quantity',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
