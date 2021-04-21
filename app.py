# in this mini app, we're implementing OAuth authentication with github and follow
# the workflow described here: https://docs.github.com/en/developers/apps/authorizing-oauth-apps

# we use the flask web framework, see here for a quickstart guide: https://flask.palletsprojects.com/en/1.1.x/quickstart/#
from flask import Flask, redirect, request, render_template, url_for

# we also use the json library to convert text responses to json objects and
# the requests library to make get and post requests
import json
import requests

# ToDo: fill in your client ID and secret you got from github.
#       remember, you don't want to commit those strings to your repository, otherwise
#       everybody who can see your code can use your github account for OAuth
client_id     = "346d4cb9716e56c96640"
client_secret = "20dc081eaae24e85072a8296d58c7f7e7c45864c"

# ToDo: add the the different URLs for using OAuth with github as constants here...
redirectURL   =  "http://localhost:5000/auth/callback"
authorizeURL  = f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirectURL}&scope=user:email"
getTokenURL   =  "https://github.com/login/oauth/access_token"

# creating the web app
app = Flask(__name__)

# the index page. for this mini app, let's assume that we handle sessions with
# url parameters. we assume that, if a user is logged in, an OAuth access token
# is passed to this function in the url.
#
# ToDo:
#  - if we don't get an access token, display a "Login with GitHub" button
#  - if we have an access token, use if to fetch the user info. use it to display
#    a greeting that includes the user's name, and a logout button
#
# there are certainly many ways to do it, but here, let's use a template that
# contains code for both cases. depending on a (possible undefined) user's name
# that we pass into the template, we decide what to display.
@app.route("/")
def index():
    access_token = request.args.get("access_token")
    username     = None
    if access_token:
        r = requests.get( "https://api.github.com/user"
                        , headers = { "Authorization" : f"token {access_token}" }
                        )
        username = json.loads(r.text)["name"]

    return render_template("index.html", username = username)


# the auth route.
#
# ToDo: redirect the user to github's authorisation url (we could do this also
#       directly with the login button)
@app.route("/auth")
def auth():
    return redirect(authorizeURL)


# the callback url where github redirects the user. we receive a code that we
# can use to get an access token for the user's account data.
#
# ToDo:
#  - use the code to get an access token
#  - redirect the user to the start page and pass the access token as a url parameter
@app.route("/auth/callback")
def callback():
    code = request.args.get("code")

    r = requests.post( getTokenURL
                     , data    =  { "client_id"     : client_id
                                  , "client_secret" : client_secret
                                  , "code"          : code
                                  }
                     , headers = { "accept": "application/json" }
                     )

    access_token = json.loads(r.text)["access_token"]

    return redirect(url_for("index", access_token = access_token))
