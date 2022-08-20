from encodings import utf_8
import praw
import time
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

cwd = os.getcwd()
t = time.ctime()
titleFile = cwd + "\\titles.js"


def pull_news(cid, cs):
    reddit = praw.Reddit(client_id=cid,
                         client_secret=cs,
                         user_agent="news ticker script",
                         redirect_uri="http://localhost:8080")

    f = open(titleFile, "w")
    f.write(time.ctime() + '~')
    f.close()
    for submission in reddit.subreddit('news').top(limit=50, time_filter="day"):
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


if __name__ == "__main__":
    pull_news(str(sys.argv[1]), str(sys.argv[2]))
