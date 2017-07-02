import urllib.request
import json

AIP_TOKEN=open("youappi_token.txt").read()
print("TOKEN:", API_TOKEN)

def run():
    print("start")

    token = API_TOKEN
    url = "https://service.youappi.com/cmp/campaigninfo?accesstoken={0}".format(token)

    content = urllib.request.urlopen(url).read()
    body = content.decode('utf-8')

    f = open("./manual.json", "w")
    f.write(body)
    f.close()

    print("end")