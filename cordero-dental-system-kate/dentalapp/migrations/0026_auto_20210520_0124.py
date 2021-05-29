# Generated by Django 3.0.14 on 2021-05-19 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dentalapp', '0025_auto_20210519_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='expiry_date',
            field=models.DateField(default=django.utils.timezone.now, error_messages={'required': 'Invalid Date Input'}),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_type',
            field=models.CharField(choices=[('Perishable', 'Perishable'), ('Non-Perishable', 'Non-Perishable')], default='Non-Perishable', max_length=25),
        ),
    ]
