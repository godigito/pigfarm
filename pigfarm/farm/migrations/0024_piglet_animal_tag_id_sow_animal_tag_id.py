# Generated by Django 5.1.6 on 2025-05-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0023_expenserecord_alter_incomerecord_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='piglet',
            name='animal_tag_id',
            field=models.CharField(blank=True, help_text='E.g., RW-PIG-001', max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='sow',
            name='animal_tag_id',
            field=models.CharField(blank=True, help_text='E.g., RW-PIG-001', max_length=50, null=True, unique=True),
        ),
    ]
