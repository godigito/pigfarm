# Generated by Django 5.1.6 on 2025-05-03 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0019_incomerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='sow',
            name='inherited_insemination_type',
            field=models.ForeignKey(blank=True, help_text='Insemination type inherited from the piglet if promoted', null=True, on_delete=django.db.models.deletion.SET_NULL, to='farm.insemination'),
        ),
    ]
