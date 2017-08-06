from adnetwork.models import Campaign
import json

def size2int(x):
    x = x.split("x")
    return int(x[0])*int(x[1])

def run():
    print("start")

    f = open("./manual.json", "r")
    body = f.read()
    res = json.loads(body)

    data = res['data']
    for id in data:
        # 'redirect_url'
        # 'campaign_id'
        # 'app_url'
        # 'max_daily'
        # 'adid_required'
        # 'creatives'
        # 'app_details'
        # 'offer_id'
        # 'cpi'
        # 'idfa_required'
        # 'countries'
        # 'capping_type'
        # 'platform'

        v = data[id]

        app_info = v['app_details']
        images = v['creatives']

        sizes = list(images.keys())
        sizes = sorted(sizes, key=size2int, reverse=True)
        app_image = app_info['app_icon'] if len(sizes) == 0 else images[sizes[0]]

        if Campaign.objects.filter(cid=v['campaign_id']).exists():
            Campaign.objects.filter(cid=v['campaign_id']).update(
                platform=v['platform'],
                price=v['cpi'],
                appstore=v['app_url'],
                redirect_url=v['redirect_url'],
                country=",".join(v['countries']),
                title=app_info['app_name'],
                description=app_info['app_description'],
                app_icon=app_info['app_icon'],
                app_image=app_image,
            )
        else:
            Campaign.objects.create(
                cid=v['campaign_id'],
                platform=v['platform'],
                price=v['cpi'],
                appstore=v['app_url'],
                redirect_url=v['redirect_url'],
                country=",".join(v['countries']),
                title=app_info['app_name'],
                description=app_info['app_description'],
                app_icon=app_info['app_icon'],
                app_image=app_image,
            )

    print("end")
    
    
    
    
    
    
    
    
from django.shortcuts import render
from django.http import HttpResponse

def callback(request):
    user_id = request.GET.get('user_id')
    click_id = request.GET.get('click_id')
    payout = request.GET.get('payout')

    AdLog.objects.create(
        user_id=user_id,
        click_id=click_id,
        payout=payout
    )

    return HttpResponse()
