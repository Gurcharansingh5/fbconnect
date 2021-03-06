import flask
# from oauthlib.oauth2.rfc6749.parameters import validate_token_parameters
import requests_oauthlib
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

FB_CLIENT_ID=2256808184449973    
FB_CLIENT_SECRET="bc5fa70ff4ff8dd693f804ba4f0db80c"
FB_AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
FB_TOKEN_URL = "https://graph.facebook.com/oauth/access_token"
URL = "https://65ad5fe37895.ngrok.io"

FB_SCOPE = ["email","ads_management"]

app = flask.Flask(__name__)


@app.route("/")
def index():
	return """
	<a href="/fb-login">Login with Facebook</a>
	"""


@app.route("/fb-login")
def login():
	facebook = requests_oauthlib.OAuth2Session(
    	FB_CLIENT_ID, redirect_uri=URL + "/fb-callback", scope=FB_SCOPE
	)
	authorization_url, _ = facebook.authorization_url(FB_AUTHORIZATION_BASE_URL)

	return flask.redirect(authorization_url)


@app.route("/fb-callback")
def callback():
	facebook = requests_oauthlib.OAuth2Session(
    	FB_CLIENT_ID, scope=FB_SCOPE, redirect_uri=URL + "/fb-callback"	)

	# we need to apply a fix for Facebook here
	facebook = facebook_compliance_fix(facebook)

	token = facebook.fetch_token(
    	FB_TOKEN_URL,
    	client_secret=FB_CLIENT_SECRET,
    	authorization_response=flask.request.url,

	)

	print(token)
	# Fetch a protected resource, i.e. user profile, via Graph API

	facebook_user_data = facebook.get(
    	"https://graph.facebook.com/me?fields=id,name,email,picture{url}"
	).json()

	print('facebook_user_data')
	print(facebook_user_data)
	email = facebook_user_data["email"]
	name = facebook_user_data["name"]
	picture_url = facebook_user_data.get("picture", {}).get("data", {}).get("url")

	return f"""
	User information: <br>
	Name: {name} <br>
	Email: {email} <br>
	Avatar <img src="{picture_url}"> <br>
	<a href="/">Home</a>
	"""

if __name__ == '__main__':
	app.run(debug=True)

