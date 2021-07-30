
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
access_token = 'EAAgEjhopC7UBAIL2J4QAEfTJxY28XZCv3lE5RF70O2vzYFTb89r8wc8zC89mpTEz3ZCJttx3H9p9bR4hNT7dZAHFLZBnEFNPDPjcPUDpzRiBoEHSvqEIKTBmvJJ6gEfg50Bv5BV7aID2NPnYnhDQWWbril5QqPnQ4ebw5rO7Vu5LyMGgugxDdP0hMzG2GBXKvUoYIjTFOwZDZD'
app_secret = 'bc5fa70ff4ff8dd693f804ba4f0db80c'
app_id = 2256808184449973 
id = 'act_144169154493518'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
create_campaign_params = {
  'name': 'My new campaign',
  'objective': 'LINK_CLICKS',
  
  'status': 'ACTIVE',
  'special_ad_categories': [],
}
campaign_id = AdAccount(id).create_campaign(
  fields=fields,
  params=create_campaign_params,
)
print ('campaign_id =============='+campaign_id['id'])

params = {
  'name': 'My Reach Ad Set',
  'optimization_goal': 'REACH',
  'billing_event': 'IMPRESSIONS',
  'bid_amount': '2000',
  'daily_budget': '100000',
  'campaign_id': campaign_id['id'],
  'targeting': {'geo_locations':{'countries':['US']},'facebook_positions':['feed']},
  'status': 'ACTIVE',
}
ad_set_id = AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)
print ('ad_set_id =============='+ad_set_id['id'])
# 525549421884373

params = {
  'name': 'new Sample Creative',
  'object_story_spec': {'page_id':100237612354550,'video_data':{'image_url':'https://avatars.githubusercontent.com/u/8880186?s=88&u=ccd6fc36312b4d34e68fff60580f18ddddc58729&v=4','video_id':527874491784763,'call_to_action':{'type':'INSTALL_MOBILE_APP','value':{'link':"https://play.google.com/store/apps/details?id=com.ludo.king"}}}},
}

adCreative = AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
)
print ('adCreative_id =============='+adCreative['id'])

params = {
  'name': 'My new Ad',
  'adset_id': ad_set_id['id'],
  'creative': {'creative_id':adCreative['id']},
  'status': 'ACTIVE',
  'object_story_spec': {'call_to_action':{'type':'LIKE_PAGE','e':{'page':"100237612354550"}}}
}
ad_id = AdAccount(id).create_ad(
  fields=fields,
  params=params,
)
print (ad_id)

