import praw
import urllib2
import json
import pafy
import time

user_agent = ("Reddit Youtube to gig v0.1 by /u/Austinto")
r = praw.Reddit(user_agent=user_agent)
r.login("RedditAutoCommentBot","pratik123")
wordsToMatch = ['!gfycatbot']
cache = []


def get_length(url):
    video = pafy.new(url)
    length=video.length
    return length

def convert_to_gif(url):
    response = urllib2.urlopen(url)
    data = json.load(response)
    return data['gifUrl']

def run_bot():
    subreddit = r.get_subreddit("YoutubetoGif")
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
                            comment.reply("Here is the Gif Version of the video : "+gifurl+"\nThis is a bot and won't answer to messages. Message to the [Owner](http://www.reddit.com/message/compose/?to=Austinto&amp;subject=BotReport) for bug reports.")
                            cache.append(comment.id)
                    else:
                        comment.reply("Length of the video should be less than 15sec.\nThis is a bot and won't answer to messages. Message to the [Owner](http://www.reddit.com/message/compose/?to=Austinto&amp;subject=BotReport)")
                        cache.append(comment.id)

while True:
    run_bot()
    time.sleep(10)
    



