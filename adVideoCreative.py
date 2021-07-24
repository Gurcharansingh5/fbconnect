import os
from facebook_business.adobjects.advideo import AdVideo
from facebook_business import FacebookSession
from facebook_business import FacebookAdsApi
from facebook_business.adobjects.advideo import AdVideo
### Setup session and api objects
session = FacebookSession(
    2256808184449973,
    'bc5fa70ff4ff8dd693f804ba4f0db80c',
    'EAAgEjhopC7UBAHFVP3N7AlZAQMZBIvq2QKLK3wDdVCVWJOLe0tTZCiWL1VOBsgsDA4nBS7ecoRGI39mNUaf8Aw3JwxrND14i2mfWe7Yn9LXigtQIzjBTfQ9z6rQwyNOrQBvZAEkMridAqZCJgabiWlRwJghltsQCmRZBEZAbKro9nfbElzDMPqL',
)

FacebookAdsApi.set_default_api(FacebookAdsApi(session))
video = AdVideo(parent_id='act_144169154493518')
video_path = os.path.join(
        os.path.dirname(__file__),'ac-ak-adslots-fail.mp4'

    )

# set video fields
video[AdVideo.Field.filepath] = video_path

# remote create
video.remote_create()
video.waitUntilEncodingReady()

print(video)