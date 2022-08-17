from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import response
import praw
import time
import os
import sys
import requests
import socket


cwd = os.getcwd()
print(cwd)
titleFile = "/home/pi/reddit-news/titles.json"
# titleFile = r"C:\MagicMirror\modules\News-Ticker\titles.json"
client_id = "p-ghimx220CYl6nMJD6gIg"
client_secret = "g_xTvLi4cfOVcJPTzdLn42w0B6jrrg"
user_agent = "news ticker script by u/hayseed_byte"
reddit = praw.Reddit(
    client_id="p-ghimx220CYl6nMJD6gIg",
    client_secret="g_xTvLi4cfOVcJPTzdLn42w0B6jrrg",
    user_agent="news ticker script by u/hayseed_byte",
    redirect_uri="http://localhost:8080",
)

print(cwd)
print("clearing titles")
f = open(titleFile, "w")
f.write('{ "titles": [')
f.close()
print("getting submissions from reddit")
for submission in reddit.subreddit('news').hot(limit=50):
    title = submission.title
    atitle = title.replace("\"", "\'")
    btitle = atitle.replace("‘", "\'")
    ctitle = btitle.replace("’", "\'")
    f = open(titleFile, "a")
    f.write('\"' + ctitle + '\"' + ", " + '\n')
    # f.write("\"" + ctitle + "\"" + ",")
    f.close()
print("finishing up")
f = open(titleFile, "r")
x = f.read()
f.close()
print("x" + x)
c = x[:-3]
print("c" + c)
f = open(titleFile, "w")
f.write(c + ' ]}')
f.close()
print("file created")

# read = open(titleFile, "r")
# x = requests.post("localhost:9111", data=read.read(), headers={
#     'Access-Control-Allow-Origin': '*',
#      })
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)


class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/home/pi/titles.json'
        try:
            # Reading the file
            file_to_open = open(self.path[1:]).read()
            print("file to open:" + file_to_open)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json'),
            self.send_header('Access-Control-Allow-Origin', '*'),
            # self.send_header('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
            self.send_header('Access-Control-Allow-Methods', 'GET'),
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(
            bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 9111), web_server)
httpd.serve_forever()
print("server up")


# raise SystemExit(0)
# os._exit(0)
# sys.exit("done")
