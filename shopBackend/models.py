from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
# we directly use django User as no extra specifications are required


class Item(models.Model):
    title = models.CharField(max_length=255)
    # name = models.CharField(max_length=255)
    price = models.FloatField()
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart_items")
    apiLink = models.TextField()
    adddedOn = models.DateTimeField(auto_now_add=True)
    category = models.CharField(default="normal", max_length=255)
    priority = models.IntegerField(default=0)

    image = models.TextField(null=True)

    availability_status = models.BooleanField(default=True)
    discount_schemes_notif_enabled = models.BooleanField(default=False)
    discount_offers = models.TextField(null=True)
    availability_notif_enabled = models.BooleanField(default=False)
    price_notif_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class Notification(models.Model):
    notif_content = models.TextField()
    assoc_item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="item_notifs")
    notif_time = models.DateTimeField(auto_now_add=True)
    # is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.notif_content[10]}..."


class ExternalNotification(models.Model):
    ext_notif_content = models.TextField()
    assoc_item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="item_external_notifs")
    ext_notif_info = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        mylist = ['available', 'price', 'discount']
        if self.ext_notif_info in mylist:
            super(ExternalNotification, self).save(*args, **kwargs)
        else:
            raise ValidationError(
                "available, price, discount are only support for ext_notif_info")


class Comment(models.Model):
    comment_content = RichTextField()
    assoc_item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="item_comments")
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_content[10]}..."


class Log(models.Model):
    history_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="history_actions")
    history_log = models.TextField()

    history_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History {self.id}"
