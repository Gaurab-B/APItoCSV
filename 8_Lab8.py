import pandas as pd
import requests

def first_api():
    client_id = "3iwTWPxViEswLNjcqb2T1Q"
    secret_key = "9IHozPnqdNTlt4Ytwlqhe5ZOeXcj9w"
    redirect_url = 'https://www.linkedin.com/in/gaurab-baral-991333216'
    auth = requests.auth.HTTPBasicAuth(client_id,secret_key)
    #<requests.auth.HTTPBasicAuth object at 0x000001D9E034FAD0>
    data = {
    'grant_type': 'password',
    'username': 'Beautiful-Handle-181',
    'password': 'Hahaha121212',
    'scope': 'read'
    }
    headers = {'User-Agent': 'My/Api/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}
    res = requests.get('https://oauth.reddit.com/r/Nepal/hot', headers = headers)
    df = pd.DataFrame(columns=['subreddit', 'title', 'selftext', 'score', 'num_comments', 'author_fullname', 'link_flair_richtext'])
    data_list = []
    #post['data'].keys()
    for post in res.json()['data']["children"]:
        data_list.append({
            'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'score': post['data']['score'],
            'num_comments': post['data']['num_comments'],
            'author_fullname': post['data']['author_fullname'],
            'link_flair_richtext': post['data']['link_flair_richtext']
        })
    df = pd.DataFrame(data_list)
    df['author_fullname'] = df['author_fullname'].str.replace('t2_', '')
    df.to_csv('Group8_Lab8_firstAPI.csv', index=False)
    return df

print(first_api())