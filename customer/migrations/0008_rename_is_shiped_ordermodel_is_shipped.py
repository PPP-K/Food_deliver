# Generated by Django 5.1 on 2024-09-20 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_ordermodel_is_shiped'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='is_shiped',
            new_name='is_shipped',
        ),
    ]
