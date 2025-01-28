import os.path
import mako.template 
import random

def get():
    d = os.path.dirname( __file__ )
    t = mako.template.Template(
            filename=f"{d}/../templates/index.html")
    return t.render(isLoggedIn=random.choice([True,False]))