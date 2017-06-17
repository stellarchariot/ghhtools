from flask import Flask, request, redirect, url_for, render_template
import os
from ghh_team_generator import get_members
from praw.exceptions import ClientException
app = Flask(__name__)

def valid_url(url):
    return ("reddit.com" in url) and ("makinghiphop" in url)

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route("/generate-teams", methods=['GET', 'POST'])
def generate_teams():
    results = None
    error = None
    url = request.args.get('url', '')
    if url:
        if valid_url(url):
            try:
                results = get_members(url)
            except ClientException, e:
                error = "Problem with connecting to the Reddit API. Please check config details."
        else:
            error = "Provided URL doesn't look like it's from reddit"
        
    return render_template('generate_teams.html', error=error, url=url, results=results)

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', 8080))
