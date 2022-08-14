from encodings import utf_8
from http.server import HTTPServer, BaseHTTPRequestHandler
import praw
import time
import os
import sys
import requests
import socket

sys.stdout.reconfigure(encoding='utf-8')

cwd = os.getcwd()
t = time.ctime()
print(time.localtime())
print(time.ctime())
titleFile = cwd + "\\titles.js"
print(titleFile)
praw_site = "reddit-news-ticker"


reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent="user agent",
                     redirect_uri="http://localhost:8080")

f = open(titleFile, "w")
f.write(time.ctime() + '~')
f.close()
print("getting submissions from reddit")
for submission in reddit.subreddit('news').hot(limit=50):
    title = submission.title
    atitle = title.replace("\"", "\'")
    btitle = atitle.replace("‘", "\'")
    ctitle = btitle.replace("’", "\'")
    f = open(titleFile, "a")
    f.write(ctitle + " ~ ")
    f.close()
f = open(titleFile, "r")
x = f.read()
f.close()
c = x[:-2]  # remove last two characters from string
f = open(titleFile, "w")
f.write(c)
f.close()
p = open(titleFile, "r")
q = p.read()
print(q)
p.close()
sys.exit(0)
