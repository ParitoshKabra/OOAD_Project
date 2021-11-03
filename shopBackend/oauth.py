import requests
from django.core.exceptions import ValidationError

CLIENT_ID = "194665914760-jka2oupgtl18kp793sjirj8blvnseui0.apps.googleusercontent.com"
CLIENT_SECRET = "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"
GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
redirect_uri = "http://127.0.0.1:3000/google/auth/"
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'


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
