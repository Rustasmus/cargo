# Generated by Django 4.0.6 on 2022-08-04 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0004_alter_driver_options_alter_invoice_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='hight',
            new_name='higth',
        ),
    ]
