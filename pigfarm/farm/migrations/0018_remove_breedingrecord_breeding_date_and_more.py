# Generated by Django 5.1.6 on 2025-04-23 09:42

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0017_sow_promoted_from_piglet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breedingrecord',
            name='breeding_date',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='injection_1_date',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='injection_2_date',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='injection_3_date',
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='expected_narrow_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='insemination_1_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='insemination_2_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='insemination_3_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='insemination_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='farm.insemination'),
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='heat_detection_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed_pregnant', 'Confirmed Pregnant'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
