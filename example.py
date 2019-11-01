# coding: utf-8

from __future__ import print_function, unicode_literals
import os
from boxsdk import Client
from boxsdk.exception import BoxAPIException
from boxsdk.object.collaboration import CollaborationRole
from auth import authenticate
from bottle import route, redirect, run
from bottle import get, post, request, Bottle

app = Bottle()

@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login')
def do_login():
    oauth, _, _ = authenticate()
    client = Client(oauth)

    # 'me' is a handy value to get info on the current authenticated user.
    me = client.user(user_id='me').get(fields=['login'])
    redirect('/message/'+me['login'])

@route('/message/<email>')
def show_user(email):
    return "The email of the user is: " + email

if __name__ == '__main__':
   run(host='0.0.0.0', port=8080)