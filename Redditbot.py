import praw
import urllib2
import json
import pafy
import time

user_agent = ("Reddit Youtube to gif v0.1 by /u/Austinto")
r = praw.Reddit(user_agent=user_agent)
r.login("YoutubeToGifBot","pratik151")



def get_length(url):
    video = pafy.new(url)
    length=video.length
    return length



def convert_to_gif(url):
    response = urllib2.urlopen(url)
    time.sleep(100)    
    response = urllib2.urlopen(url)
    data = json.load(response)
    gifurl = data['gifUrl']
    gifurl = gifurl.replace("http://giant.","")
    gifurl = gifurl.replace(".gif","")
    gifurl = "http://"+gifurl
    return gifurl


def run_bot():
    subreddit = r.get_subreddit("leagueoflegends")
    for submission in subreddit.get_rising(limit=30):
        url = submission.url
        if "youtu" in url:
            if get_length(url) <= 15:
                if submission.id not in open('Reddit','r').read().split(','):
                    url1 = "http://upload.gfycat.com/transcode?fetchUrl="+url+"&fetchSeconds=0&fetchMinutes=0&fetchHours=0&fetchLength="+str(get_length(url))
                    gifurl = convert_to_gif(url1)
                    submission.add_comment("Here is the Gif Version of the video : "+gifurl+"."+"\n\n---------------------------------------------------\n\nThis is a bot and won't answer to messages. Message to the [Owner](http://www.reddit.com/message/compose/?to=Austinto&amp;subject=BotReport) for bug reports.")
                    open('Reddit','a').write(','+submission.id)

while True:
    run_bot();
    time.sleep(5)

