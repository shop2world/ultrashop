# Generated by Django 3.2.4 on 2021-08-05 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210805_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modify_date',
        ),
    ]
