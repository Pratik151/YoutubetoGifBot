import praw
import urllib2
import json
import pafy

user_agent = ("Reddit Youtube to gig v0.1 by /u/Austinto")
r = praw.Reddit(user_agent=user_agent)
r.login("RedditAutoCommentBot","pratik123")
wordsToMatch = ['!gfycatbot']
cache = []

def get_length(url):
    video = pafy.new(url)
    length=video.length
    return length

def run_bot():
    subreddit = r.get_subreddit("test")
    for submission in subreddit.get_hot(limit=1):
        comments = submission.comments
        for comment in comments:
            text = comment.body
            isMatch = any(string in text for string in wordsToMatch)
            if isMatch:
                url = submission.url
                if "youtu" in url:
                    if get_length(url) <= 15:
                        url1 = "http://upload.gfycat.com/transcode?fetchUrl="+url+"&fetchSeconds=0&fetchMinutes=0&fetchHours=0&fetchLength="+str(get_length(url))
                        gifurl = convert_to_gif(url1)
                        if comment.id not in cache:




def convert_to_gif(url):
    response = urllib2.urlopen(url)
    data = json.load(response)
    return data['gifUrl']

