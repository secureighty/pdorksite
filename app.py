import flask
import json
import urllib.parse
import os
import requests
app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Welcome. Supply a \"query=\" parameter for /site to get a new site."


@app.route('/site')
def site():
    return get_site(flask.request.args.get('query'))

@app.route('/seo')
def seo():
    return flask.redirect("https://pastebin.com/UWkKnwUe", 302)

def get_site(query):
    subscriptionKey = ''
    endpoint = 'https://api.bing.microsoft.com'
    customConfigId = 'e5f9a53e-48fa-4b66-9d43-9b52fb158d18'
    searchTerm = urllib.parse.quote_plus("site:pastebin.com <!DOCTYPE html> " + query)
    command = f'curl --header "Ocp-Apim-Subscription-Key:{subscriptionKey}" "{endpoint}/v7.0/custom/search?q={searchTerm}%20&customconfig={customConfigId}&mkt=en-US" -o output.txt'
    print(command)
    os.system(command)
    searchresult = {}
    with open("output.txt") as f:
        searchresult = json.loads(f.read())
    firsturl = searchresult["webPages"]["value"][0]["url"]
    firsturl = firsturl[:20]+'/raw'+firsturl[20:]

    return requests.get(firsturl).text

app.run()
