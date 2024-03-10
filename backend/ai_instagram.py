import sys
from flask import Flask, request, redirect
import json
import urllib3
import logging

app = Flask(__name__)

http = urllib3.PoolManager()

app_id = "395889439750144"
app_secret = "93d74045fcbeb4737d9ebea879ea10dc"
redirect_uri = "https://tom123277.github.io/auth"

app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler('app.log')  # Log to a file
app.logger.addHandler(handler)

@app.route('/')
def home():
    return "Home page!"

@app.route('/insta')
def get_auth_code():
    get_authorization = http.request("GET", f"https://api.instagram.com/oauth/authorize?client_id={app_id}&redirect_uri={redirect_uri}&scope=user_profile,user_media&response_type=code")

    try:
        if get_authorization.status == 200:
            authorized_url = get_authorization.url
            app.logger.info(f"Authorized url:{authorized_url}")
            return redirect(authorized_url)
        else:
            return "Auth Error"
    except Exception as e:
        app.logger.error(f"Error: {e}")

@app.route('/auth')
def handle_auth():
    redirect_uri = "https://tom123277.github.io"
    auth_code = request.args.get('code')
    app.logger.info(f"Auth code:{auth_code}")

    get_access_token = http.request(
        "POST",
        f"https://api.instagram.com/oauth/access_token",
        fields={
            'client_id': app_id,
            'client_secret': app_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': auth_code
        }
    )

    if get_access_token.status == 200:
        data = json.loads(get_access_token.data.decode('utf-8'))
        app.logger.info(data)
        access_token = data["access_token"]
        user_id = data["user_id"]

        # Now you have the access token and user ID
        print("Access Token:", access_token)
        print("User ID:", user_id)
        return f"Access Token: {access_token}<br>User ID: {user_id}"
    else:
        return "Error getting access token"

if __name__ == '__main__':
    app.run(debug=True)
