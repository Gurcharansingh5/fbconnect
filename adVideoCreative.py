import os
from facebook_business.adobjects.advideo import AdVideo
from facebook_business import FacebookSession
from facebook_business import FacebookAdsApi
from facebook_business.adobjects.advideo import AdVideo
### Setup session and api objects
session = FacebookSession(
    2256808184449973,
    'bc5fa70ff4ff8dd693f804ba4f0db80c',
    'EAAgEjhopC7UBAKRK7wafwZAxwFOG67a0IHZCU1pOTV74m3ZAAZBXvXUueZCAZCtyWJPg49qPaWSaMBLLAUI5QIdz6dQrZBtyhaqtMpIrNekvG4pkXrbRZBZAOnP3onxpoWoenbTN99TOYzqUCSPcLdMu1DyCKsijvVAZBXEOH86APqUWl6I8NWvB5SQzkZBwCb8RtEZD',
)

FacebookAdsApi.set_default_api(FacebookAdsApi(session))
video = AdVideo(parent_id='act_534146227796276')
video_path = os.path.join(
        os.path.dirname(__file__),'ac-ak-adslots-fail.mp4'

    )

# set video fields
video[AdVideo.Field.filepath] = video_path

# remote create
video.remote_create()
video.waitUntilEncodingReady()

print(video)