import pandas as pd
import requests

def first_api(): #REDDIT API
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
    print(df)
    print("\nFile saved as Group8_Lab8_firstAPI.csv")
    df.to_csv('Group8_Lab8_firstAPI.csv', index=False)

def second_api(): #Harry Potter API
    while True:
        try:
            print("---------------------------------------------------------------------------")
            choice = int(input("Enter:\n 1: For extracting information of Harry Potter Characters. \n 2: For extracting information of Harry Potter Spells. \n 3: Go Back \n 4: End the Program\n-------------------------------------------------------------------\n"))
        except:
            print("Enter a numeric value")
        if choice == 1:
            url1 = "https://hp-api.onrender.com/api/characters"
            response = requests.get(url1)
            data = response.json()
            df = pd.DataFrame(data)
            df.to_csv('Group8_Lab8_HarryPotterCharacters.csv', index=False)
            print(df)
            print("\nFile Saved as Group8_Lab8_HarryPotterCharacters.csv")
            second_api()
            return df
        elif choice == 2:
            url2 = "https://hp-api.onrender.com/api/spells"
            response2 = requests.get(url2)
            a1 = response2.json()
            df2 = pd.DataFrame(a1)
            df2.to_csv('Group8_Lab8_HarryPotterSpells.csv', index=False)
            print(df2)
            print("\nFile Saved as Group8_Lab8_HarryPotterSpells.csv")
            second_api()
            return df2
        elif choice == 3:
            print("Going back to the previous screen")
            break
        elif choice == 4:
            exit(1)
        else:
            print("Invalid choice. Please enter a valid option.")

def third_api(): #DOG FACT API
    url = "https://dogapi.dog/api/v2/breeds"
    response = requests.get(url)
    data = response.json()
    breeds_data = data.get('data', [])
    final_data = [entry.get('attributes', {}) for entry in breeds_data]
    df3 = pd.DataFrame(final_data)
    columns_to_drop = ['life', 'male_weight','female_weight']
    df3 = df3.drop(columns=columns_to_drop)
    print(df3)
    df3.to_csv('Group8_Lab8_DogFacts.csv', index=False)
    print("\nFile Saved as Group8_Lab8_DogFacts.csv")

def fourth_api(): #CLASH OF CLANS API
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQ4NTUyNjc2LTEzZDgtNDBlOC05M2ZjLTcxNWFkNjNlNDVkOCIsImlhdCI6MTcwMDg2NzU5NSwic3ViIjoiZGV2ZWxvcGVyLzQ0YTJiMjU0LWRlNzQtNjBhYy0xZGY1LWU2NzYzYzM3ZGY5YiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjU0Ljg2LjUwLjEzOSIsIjk4LjIyMy4xMDQuMTciXSwidHlwZSI6ImNsaWVudCJ9XX0.Md1Y08nUEjpJ1fBiIsNm_tr0Ic6NFSh0zpOTq695KNvubefmSKHZzX1MDMqm4lKlswh1HSUBEKCk_6cA_W3ZCA',
    'Accept': 'application/json'
    }
    response = requests.get('https://api.clashofclans.com/v1/players/%238J9P8Y0LV', headers=headers)
    user_json = response.json()
    df = pd.json_normalize(user_json)
    print(df)
    df.to_csv('Group8_Lab8_ClashofClans.csv', index = False)
    print("\nFile Saved as Group8_Lab8_ClashofClans.csv")

if __name__ == "__main__": #Menu for the 4 API
    while True:
        print("------------------------------------------------------------------")
        print("Welcome to API Extraction System built by group 8. What would you like to do?")
        print("Enter:\n1: Get Data about r/Nepal in reddit.(Extract Reddit API)\n2: Get Data about Harry Potters.(Extract Harry Potter API)\n3: Get Data about Dogs.(Extract Dog API)\n4: Get Data about Clash of Clans(Extract Clash of Clans API)\n5: Exit")
        print("-----------------------------------------------------------------")
        try:
            choice = int(input())
        except:
            print("Please Enter a valid number")
        if choice == 1:
            first_api() #Reddit
        elif choice ==2:
            second_api() #Harry Potter
        elif choice ==3:
            third_api() #Dog Facts
        elif choice ==4:
            fourth_api()
        elif choice ==5:
            exit() #End the Program
        else:
            print(" Invalid choice. Please enter a valid option.")
        