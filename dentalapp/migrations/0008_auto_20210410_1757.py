# Generated by Django 3.0.3 on 2021-04-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalapp', '0007_auto_20210228_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='contact_person',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='special_notes',
            field=models.TextField(default=None, max_length=100),
        ),
    ]
