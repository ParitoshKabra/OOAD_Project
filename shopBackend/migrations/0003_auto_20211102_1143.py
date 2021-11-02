# Generated by Django 3.2.8 on 2021-11-02 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopBackend', '0002_notification_is_viewed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='notif_enabled',
            new_name='availability_notif_enabled',
        ),
        migrations.RemoveField(
            model_name='item',
            name='descp',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_viewed',
        ),
        migrations.AddField(
            model_name='item',
            name='adddedOn',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='apiLink',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price_notif_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]