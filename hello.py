#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

import os


print('Content-Type: text/html\n')
print()

print('<!DOCTYPE html>\n<html><body>')

print('<h1>os.environ</h1>')
print(dict(os.environ))

# print the keys in order, to make them easier to search
print('<h1>Environment variables</h1><table><tbody>')
print('<tr><th>Key</th><th>Value</th></tr>')
for k in sorted(os.environ.keys()):
    print('<tr><td>{k}</td><td>{v}</td></tr>'.format(
        k=k, v=os.environ[k]))
print('</tbody></table>')

print('<h1>QUERY_STRING</h1>')
print(os.environ['QUERY_STRING'])

print('<h1>User Agent</h1>')
print(os.environ['HTTP_USER_AGENT'])

print('</body></html>')


