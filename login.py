#!/usr/bin/env python3

from http.cookies import SimpleCookie
import cgi, cgitb
cgitb.enable()

from templates import login_page, after_login_incorrect, secret_page
import secret

import os

s = cgi.FieldStorage()
u = s.getfirst('username')
w = s.getfirst('password')

print('Content-Type: text/html')

if u == secret.username and w == secret.password:
    print('Set-Cookie: username={u}\nSet-Cookie: password={w}'.format(
        u=u, w=w))

c = SimpleCookie(os.environ['HTTP_COOKIE'])
cu = None
cw = None
if c.get('username'): cu = c.get('username').value
if c.get('password'): cw = c.get('password').value

if cu == secret.username and cw == secret.password:
    u = cu
    w = cw


logged_in = (u == secret.username and w == secret.password)


print()
if logged_in:
    print(secret_page(username=u, password=w))
elif (w or u):
    print(after_login_incorrect())
else:
    print(login_page())


#if (w or u):
#    print('<h1>Effective login</h1>')
#    print('Username = {u}<br />Password = {w}'.format(u=u, w=w))
