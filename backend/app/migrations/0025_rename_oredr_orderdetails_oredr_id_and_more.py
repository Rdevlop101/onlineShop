# Generated by Django 4.2 on 2023-06-16 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_rename_user_orders_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='oredr',
            new_name='oredr_id',
        ),
        migrations.RenameField(
            model_name='orderdetails',
            old_name='product',
            new_name='product_id',
        ),
    ]
