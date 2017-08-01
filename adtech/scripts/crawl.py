import urllib.request
import json

API_TOKEN=open("abcnetwork_token.txt").read()
print("TOKEN:", API_TOKEN)

def run():
    print("start")

    token = API_TOKEN
    url = "https://service.abc.com/cmp/campaigninfo?accesstoken={0}".format(token)

    content = urllib.request.urlopen(url).read()
    body = content.decode('utf-8')

    f = open("./manual.json", "w")
    f.write(body)
    f.close()

    print("end")
