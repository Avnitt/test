# Generated by Django 5.0 on 2023-12-22 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_remove_slot_professional_slot_booked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='flag',
            field=models.IntegerField(default=1),
        ),
    ]
