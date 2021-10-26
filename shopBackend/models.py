from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
# we directly use django User as no extra specifications are required


class Item(models.Model):
    title = models.CharField(max_length=255)
    descp = RichTextField()
    price = models.FloatField()
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart_items")
    availability_status = models.BooleanField(default=True)
    category = models.CharField(default=None, max_length=255)
    notif_enabled = models.BooleanField(default=False)
    apiLink= models.CharField(max_length=255)
    adddedOn= models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.title}"


class Notification(models.Model):
    notif_content = models.TextField()
    assoc_item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="item_notifs")
    notif_time = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.notif_content[10]}..."


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
    history_log = models.CharField(max_length=511)

    history_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History {self.id}"
