# Generated by Django 3.0.2 on 2021-04-18 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentalapp', '0014_auto_20210416_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='required_material',
            name='quantity_unit',
        ),
    ]
