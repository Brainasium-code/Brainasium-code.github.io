from flask import Flask, render_template,jsonify
from flask_sock import Sock
from datetime import date

app = Flask(__name__)
sock = Sock(app)


# @sock.route('/echo')
# def echo(ws):
#     while True:
#         data = ws.receive()
#         ws.send(data)

@sock.route('/ws_log')
def ws_log(ws):
    while True:
        data = {
            'type': "message",
            'text': 'this is a test',
            'id':   'Connor',
            'date': str(date.today),
        }
        ws.send(data)


# set FLASK_APP=ws_demo.py
# flask run