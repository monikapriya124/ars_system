# Generated by Django 5.1.6 on 2025-03-08 08:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='seat_number',
        ),
        migrations.AddField(
            model_name='reservation',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
