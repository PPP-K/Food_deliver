# Generated by Django 5.1 on 2024-09-18 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_ordermodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='zip_code',
            new_name='pin_code',
        ),
    ]
