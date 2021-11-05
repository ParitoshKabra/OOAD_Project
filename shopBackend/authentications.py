from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
import json


class CheckUser(ModelBackend):
    def authenticate(self, request, user_json):
        try:
            print(user_json)
            user = User.objects.get(username=user_json['email'].lower(
            ))
            return user
        except User.DoesNotExist:
            user = User.objects.create(
                username=user_json['email'].lower(
                ), first_name=user_json['given_name'], last_name=user_json['family_name'], name=f"{user_json['given_name']} {user_json['family_name']}"
            )
            return user

    def get_user(self, user_id: int):
        return super().get_user(user_id)
