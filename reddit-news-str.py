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
    f.write(time.ctime() + '~')  # timestamp for start of ticker
    f.close()
    # top 50 posts for the day
    for submission in reddit.subreddit('news').hot(limit=50):
        title = submission.title
        atitle = title.replace("\"", "\'")
        btitle = atitle.replace("‘", "\'")
        ctitle = btitle.replace("’", "\'")
        f = open(titleFile, "a")
        # add ~ between each title so we can replace it later (it is unlikely to be in a title)
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
    # print titles all at once so it's sent to stdout to be picked up by node_helper.js
    print(q)
    p.close()
    sys.exit(0)


if __name__ == "__main__":
    pull_news(str(sys.argv[1]), str(sys.argv[2]))
