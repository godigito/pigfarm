# Generated by Django 5.1.6 on 2025-03-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0003_alter_breedingrecord_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breedingrecord',
            name='actual_farrow_date',
        ),
        migrations.RemoveField(
            model_name='breedingrecord',
            name='total_piglets_born',
        ),
        migrations.AddField(
            model_name='breedingrecord',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending 21-Day Confirmation'), ('pregnant', 'Pregnant'), ('failed', 'Failed')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='breeding_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='breedingrecord',
            name='heat_detection_date',
            field=models.DateField(default='2025-01-01'),
            preserve_default=False,
        ),
    ]
