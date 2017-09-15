from flask import Flask,request
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
#    try:
#        visits = redis.incr("counter")
#    except RedisError:
#        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = """
<b>Hostname:</b> {hostname}<br/>
<b>Remote IP:</b> {remoteip}
"""
    return html.format(hostname=socket.gethostname(),remoteip=request.remote_addr)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)