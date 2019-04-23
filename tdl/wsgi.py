"""
WSGI config for tdl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application
import threading, requests, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tdl.settings")
application = Cling(get_wsgi_application())

def awake():
    while 1:
        try:
            print("Start Awaking")
            requests.get("http://toudai-league.herokuapp.com/")
            print("End")
        except:
            print("error")
        time.sleep(60*10)

t = threading.Thread(target=awake)
t.start()
