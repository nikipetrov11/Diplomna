# Generated by Django 4.1.1 on 2022-10-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_add_date_of_event_field_to_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='next_change',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='next_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
