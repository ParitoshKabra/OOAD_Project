# Generated by Django 3.2.6 on 2021-11-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopBackend', '0002_alter_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.TextField(null=True),
        ),
    ]