# Generated by Django 3.2.4 on 2021-07-11 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_prduct_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingadress',
            old_name='adress',
            new_name='address',
        ),
    ]
