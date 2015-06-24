import praw
import urllib2
import json
import pafy
import time

user_agent = ("Reddit Youtube to gif v0.1 by /u/Austinto")
r = praw.Reddit(user_agent=user_agent)
r.login("REDDIT_USERNAME","PASSWORD")
subreddit = r.get_subreddit("SUBREDDIT_NAME")

"""
urlError Exception is raised when there is error in getting video length.
Like Error in getting video data(Video blocked) or invalid url.
"""
class urlError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "Error in Getting length of Video"
    

def get_length(url):
    try:
        video = pafy.new(url)
        length=video.length
        return length
    except:
        raise urlError



def convert_to_gif(url):
    response = urllib2.urlopen(url)
    time.sleep(200)
    response = urllib2.urlopen(url)
    data = json.load(response)
    gifurl = data['gifUrl']
    gifurl = gifurl.replace("http://giant.","")
    gifurl = gifurl.replace(".gif","")
    gifurl = "http://"+gifurl
    return gifurl


def run_bot():
    print "Grabbing Submissions"
    for submission in subreddit.get_rising(limit=30):
        if "youtu" in submission.domain:
            try:
                url = submission.url
                if get_length(url) <= 15:
                    if submission.id not in open('Reddit','r').read().split(','):
                        print "Making gif of "+submission.title
                        url1 = "http://upload.gfycat.com/transcode?fetchUrl="+url+"&fetchSeconds=0&fetchMinutes=0&fetchHours=0&fetchLength="+str(get_length(url))
                        gifurl = convert_to_gif(url1)
                        submission.add_comment("Here is the Gif Version of the video : "+gifurl+"."+"\n\n---------------------------------------------------\n\nThis is a bot and won't answer to messages. Message to the [Owner](http://www.reddit.com/message/compose/?to=Austinto&amp;subject=BotReport) for bug reports.")
                        open('Reddit','a').write(','+submission.id)
            except urlError:
                open('Reddit','a').write(','+submission.id)

while True:
    run_bot();
    time.sleep(5)

