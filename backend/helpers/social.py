from urllib.request import urlopen
from json import loads
from dateutil.parser import parse
from urllib.request import urlretrieve
from base64 import b64encode
from os import remove
import requests


def get_facebook_info(token):
    url = "https://graph.facebook.com/v2.10/me?access_token={}&fields={}"

    fields = [
        'id', 'first_name', 'last_name',
        'website', 'gender', 'picture', 'locale',
        'email', 'about', 'birthday', 'education',
        'location', 'work'
    ]
    url = url.format(token, ",".join(fields))
    user_data = loads(urlopen(url).read())

    #read user pic
    url = 'https://graph.facebook.com/v2.10/me/picture?access_token={}&width=400&height=400'.format(token)
    content = b64encode(urlopen(url).read()).decode('utf-8')

    user = {
        'email': user_data['email'],
        'first_name': user_data['first_name'],
        'last_name': user_data['last_name'],
        'gender': user_data['gender'],
        'pic': content,
        'about': user_data['about'],
        'birthday': parse(user_data['birthday']),
        'education': user_data['education'],
        'location': user_data['location']['name'],
        'work': user_data['work'],
        
        'external_accounts': {
            'facebook': {
                'id': user_data['id']
            }
        }
    }
    return user

def get_linkedin_data(user_data):
    user = {
        'email': user_data['emailAddress'],
        'first_name': user_data['firstName'],
        'last_name': user_data['lastName'],
        'pic': user_data['pictureUrls']['values'][0],
        'title': user_data['headline'],
        'about': user_data['summary'],
        'location': user_data['location']['name'],
        'external_accounts': {
            'linkedin': {
                'id': user_data['id']
            }
        }
    }
    user['pic'] = b64encode(urlopen(user['pic']).read()).decode('utf-8')
    return user
