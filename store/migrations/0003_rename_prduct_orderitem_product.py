# Generated by Django 3.2.4 on 2021-07-05 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='prduct',
            new_name='product',
        ),
    ]
