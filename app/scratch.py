import requests
import json
import os
from utils import config2

# Configurando keys de acesso
API_KEY = config2.API_KEY
API_SECRET_KEY = config2.API_SECRET_KEY
BEARER_TOKEN = config2.BEARER_TOKEN


def auth():
    return BEARER_TOKEN

def create_url():
    query="from:twitterdev -is:retweet"
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if(response.status_code!=200):
        raise Exception(response.status_code, response.text)
    return response.json()    

def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__=="__main__":
    main()