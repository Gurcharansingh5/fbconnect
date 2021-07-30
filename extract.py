# external imports
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

import os
import json

from adVideoCreative import get_video_creative_id_from_file
access_token = 'EAAgEjhopC7UBANIosjWMEPQ9isBFf9nJsszL0Peu5HBCw8iB84jdgT8tKemhzatMh40HZC3fzBqBrFZA42WX6vee4RGAAYiHhG94wb0e9tkgWKdf3DfX5VDPZAc2PZBU5aKZBAHejluTm4988RPCWqn3OmcAbLZC6QmQk4WAaYMacQdyKJGKyZB'
app_secret = 'bc5fa70ff4ff8dd693f804ba4f0db80c'
app_id = 2256808184449973 
id = 'act_144169154493518'
FacebookAdsApi.init(access_token=access_token)

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d
ready_directory_str = json.dumps(path_to_dict('READY'))
ready_directory = json.loads(ready_directory_str)
print(ready_directory)


for campaigns in ready_directory['children']:
    # print(campaigns['name'])

    create_campaign_params = {
                'name': campaigns['name'],
                'objective': 'LINK_CLICKS',
                
                'status': 'ACTIVE',
                'special_ad_categories': [],
    }

    campaign_id = AdAccount(id).create_campaign(fields=[],params=create_campaign_params)
    print ('campaign_id =============='+campaign_id['id'])

    if 'children' in campaigns:
        for adsets in campaigns['children']:
            # print(adsets['name'])
            create_ad_set_params = {
                'name': adsets['name'],
                'optimization_goal': 'REACH',
                'billing_event': 'IMPRESSIONS',
                'bid_amount': '2000',
                'daily_budget': '100000',
                'campaign_id': campaign_id['id'],
                'targeting': {'geo_locations':{'countries':['US']},'facebook_positions':['feed']},
                'status': 'ACTIVE',
            }
            ad_set_id = AdAccount(id).create_ad_set(fields=[],params=create_ad_set_params,)
            print ('ad_set_id =============='+ad_set_id['id'])

            if 'children' in adsets:
                for ads in adsets['children']:
                    print('READY'+'/'+ready_directory['children'][0]['name']+'/'+adsets['name']+'/'+ads['name'])

                    video_ID = get_video_creative_id_from_file('READY'+'/'+campaign['children'][0]['name']+'/'+adsets['name']+'/'+ads['name'])
                    print(video_ID)
                    create_ad_creative_params = {
                        'name': 'new Sample Creative',
                        'object_story_spec': {'page_id':100237612354550,'video_data':{'image_url':'https://avatars.githubusercontent.com/u/8880186?s=88&u=ccd6fc36312b4d34e68fff60580f18ddddc58729&v=4','video_id':video_ID,'call_to_action':{'type':'INSTALL_MOBILE_APP','value':{'link':"https://play.google.com/store/apps/details?id=com.ludo.king"}}}},
                    }

                adCreative = AdAccount(id).create_ad_creative(fields=[],params=create_ad_creative_params,)
                print ('adCreative_id =============='+adCreative['id'])

                create_ad_params = {

                    'name':ads['name'],
                    'adset_id': ad_set_id['id'],
                    'creative': {'creative_id':adCreative['id']},
                    'status': 'ACTIVE',
                    'object_story_spec': {'call_to_action':{'type':'LIKE_PAGE','e':{'page':"100237612354550"}}}
                    }
                ad_id = AdAccount(id).create_ad(fields=[],params=create_ad_params)
                print ('ad_id =============='+ad_id['id'])
                print('READY'+'/'+ready_directory['children'][0]['name']+'/'+adsets['name']+'/'+ads['name'])
    

