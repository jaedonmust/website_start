import os.path
import mako.template 
import mako.lookup

def get():
    d = os.path.dirname( __file__ )
    t = mako.template.Template(
            filename=f"{d}/../templates/posts.html")
    return t.render()