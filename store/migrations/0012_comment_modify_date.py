# Generated by Django 3.2.4 on 2021-08-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_comment_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
