# Generated by Django 3.2.8 on 2021-11-06 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopBackend', '0006_item_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='deleted',
        ),
    ]