import os.path
import mako.template 
import mako.lookup

lookup = mako.lookup.TemplateLookup(
    directories=[
        os.path.dirname(__file__),
        f"{os.path.dirname(__file__)}/../templates" 
    ]
)

def get():
    d = os.path.dirname( __file__ )
    t = lookup.get_template("/signup.html")
    return t.render()