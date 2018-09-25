import requests
import urllib3
import json
import argparse

urllib3.disable_warnings()

parser = argparse.ArgumentParser()
parser.add_argument("hash", help="the hash value as shown in the URL, e.g. https://app2.sli.do/event/<THIS>/questions")
parser.add_argument("event", help="the eventId")
parser.add_argument("question", help="the questionId")
parser.add_argument("votes", help="the number of votes you'd like it to place")
args = parser.parse_args()

vote_count = 0

def get_hash(hash):
    endpoint = f"https://app2.sli.do/api/v0.5/events?hash={hash}"
    res = requests.get(endpoint, verify=False)
    
    if res.status_code==200:
        res = res.json()
        return res[0]['uuid']
    else:
        return False

def get_auth(uuid):
    endpoint = f"https://app2.sli.do/api/v0.5/events/{uuid}/auth"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    res = requests.post(endpoint, headers=headers, verify=False)

    if res.status_code==200:
        res = res.json()
        return res['access_token']
    else:
        return False

def like(hash, eventId, questionId):
    global vote_count

    uuid = get_hash(hash)
    bearer = get_auth(uuid)

    endpoint = f"https://app2.sli.do/api/v0.5/events/{eventId}/questions/{questionId}/like"
    data = {"score":1}
    headers = {
        "Authorization":f"Bearer {bearer}",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    
    res = requests.post(endpoint,json=data,headers=headers, verify=False)

    if res.status_code==200:
        print(".", end="", flush=True)
        vote_count += 1


for i in range(0, int(args.votes)):
    like(args.hash, args.event, args.question)

if vote_count>0:
    print()
    print(f"Successfully voted {vote_count} times")
