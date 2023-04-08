import praw
import urllib.request

# with open('pw.txt','r') as f:
#     pw=f.read()

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', client_secret='YOUR_SECRET_KEY', user_agent='YOUR_APP_NAME',username='YOUR_USERNAME',password='YOUR_PASSWORD')

subreddit_name = 'SUBREDDIT_NAMES'

subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(limit=10)

for post in top_posts:
    if 'jpg' in post.url or 'png' in post.url:
        image_url = post.url
        filename = post.id + '.' + image_url.split('.')[-1]
        urllib.request.urlretrieve(image_url, filename)
        print('Downloaded:', filename)
