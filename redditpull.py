CLIENT_ID = 'EPpClFoAyCJoGjJkewoBNw'
SECRET_KEY = 'MBnpc9cHZXzCJOtTk_ydkdYCC-udUA'

import requests
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data = {
    'grant_type': 'password',
    'username': 'supremecruncher',
    'password': 'Nautica2004$supreme'
}

headers = {'User-Agent': 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth = auth, data = data, headers = headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

res = requests.get('https://oauth.reddit.com/r/AmItheAsshole/hot', headers = headers)

title = ""
body = ""

for post in res.json()['data']['children'][2:]:
    title = post['data']['title']
    body = post['data']['selftext']
    break


print(title)

