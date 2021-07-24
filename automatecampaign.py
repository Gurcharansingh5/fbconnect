
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.advideo import AdVideo
import os

access_token = 'EAAgEjhopC7UBAKRK7wafwZAxwFOG67a0IHZCU1pOTV74m3ZAAZBXvXUueZCAZCtyWJPg49qPaWSaMBLLAUI5QIdz6dQrZBtyhaqtMpIrNekvG4pkXrbRZBZAOnP3onxpoWoenbTN99TOYzqUCSPcLdMu1DyCKsijvVAZBXEOH86APqUWl6I8NWvB5SQzkZBwCb8RtEZD'
app_secret = 'bc5fa70ff4ff8dd693f804ba4f0db80c'
app_id = 2256808184449973
id = 'act_534146227796276'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
create_campaign_params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
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
  'bid_amount': '2',
  'daily_budget': '100000',
  'campaign_id': campaign_id['id'],
  'targeting': {'geo_locations':{'countries':['US']},'facebook_positions':['feed']},
  'status': 'PAUSED',
}
ad_set_id = AdAccount(id).create_ad_set(
  fields=fields,
  params=params,
)
print ('ad_set_id =============='+ad_set_id['id'])
# 525549421884373

params = {
  'name': 'Sample Creative',
  'object_story_spec': {'page_id':102618138787955,'video_data':{'image_url':'https://avatars.githubusercontent.com/u/8880186?s=88&u=ccd6fc36312b4d34e68fff60580f18ddddc58729&v=4','video_id':525549421884373,'call_to_action':{'type':'LIKE_PAGE','value':{'page':102618138787955}}}},
}

adCreative = AdAccount(id).create_ad_creative(
  fields=fields,
  params=params,
)
print ('adCreative_id =============='+adCreative['id'])

params = {
  'name': 'My Ad',
  'adset_id': ad_set_id['id'],
  'creative': {'creative_id':adCreative['id']},
  'status': 'PAUSED',
}
ad_id = AdAccount(id).create_ad(
  fields=fields,
  params=params,
)
print ('ad_id =============='+ad_id)

