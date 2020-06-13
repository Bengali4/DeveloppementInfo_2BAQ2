import cherrypy
import os
from hashlib import pbkdf2_hmac
from os import urandom
import json


def hashPswd(pswd, salt=None):
    if salt is None:
        salt = urandom(32)
    H = pbkdf2_hmac('sha256', pswd.encode('utf8'), salt, 100000)
    return H, salt


class WebApp():
    def __init__(self):
        self.dicologin = {}

    @cherrypy.expose
    def form(self, login="", password=""):
        with open('login.json') as file:
            content = file.read()
            self.dicologin = json.loads(content)
        with open('login.json', 'w') as file:
            self.dicologin[login] = password
            json.dump(self.dicologin, file)

        return "Hello world!"


access_log = cherrypy.log.access_log
for handler in tuple(access_log.handlers):
    access_log.removeHandler(handler)
cherrypy.quickstart(WebApp(), '', 'server.conf')
