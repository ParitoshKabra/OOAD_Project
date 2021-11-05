import requests
from django.core.exceptions import ValidationError
from .oauthUtils.constants import *


def exchange_code(code):
    access_token = get_access_token(code)
    res = requests.get(GOOGLE_USER_INFO_URL, params={
                       'access_token': access_token})
    if not res.ok:
        raise ValidationError('Failed to obtain user info from Google.')
    return res.json()


def get_access_token(code):
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    res = requests.post(GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)

    if not res.ok:
        raise ValidationError('Failed to obtain access token from Google.')

    access_token = res.json()['access_token']

    return access_token
