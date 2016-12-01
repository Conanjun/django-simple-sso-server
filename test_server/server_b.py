# coding: utf8

import os
from datetime import timedelta
from flask import Flask, session, redirect, url_for, request
import urllib

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds=24 * 60 * 60)

@app.route('/')
def index():
    session.permanent = False
    ticket = request.args.get('ticket', None)
    if ticket is not None:
        session['login_id'] = ticket.strip()
    if 'login_id' in session:
        return '登录成功'
    else:
        referer = urllib.quote('http://127.0.0.1:8887/')
        return redirect('http://127.0.0.1:8000/sso/login?referer=' + referer)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8887"),
        debug=True
    )