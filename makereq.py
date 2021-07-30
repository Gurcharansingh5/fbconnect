import requests
r = requests.get('https://graph.facebook.com/v11.0/me/adaccounts?access_token=EAAgEjhopC7UBAJHLBhEIhVThaFeSSOgdTrGk2HWZCdnhQxPr1tVNs1ZA4RtqzDTBcVrhy8VX234J0DSb2tds7IZAVodnPLZBA9ZALte1VrrGTPZASLdiQUE1OOdJ7f5q4Pzk1TPVI6ZBxmdn7ifywWEXmZBBsMEJZCgsIwlvYttEsm6hjT70ZCWQ7KkpkNja7HQtoZD').json()
ad_account_id= r['data'][0]['id']
print('ad_account_id '+ad_account_id)
r = requests.get('https://graph.facebook.com/v11.0/me/accounts?access_token=EAAgEjhopC7UBAJHLBhEIhVThaFeSSOgdTrGk2HWZCdnhQxPr1tVNs1ZA4RtqzDTBcVrhy8VX234J0DSb2tds7IZAVodnPLZBA9ZALte1VrrGTPZASLdiQUE1OOdJ7f5q4Pzk1TPVI6ZBxmdn7ifywWEXmZBBsMEJZCgsIwlvYttEsm6hjT70ZCWQ7KkpkNja7HQtoZD').json()
page_id = r['data'][0]['id']
print('page_id '+page_id)
# https://graph.facebook.com/v10.0/me/adaccounts?access_token=<access_token_from_step_3>
