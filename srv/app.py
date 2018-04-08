from flask import Flask

from endpoints import home


app = Flask('video-rental-manager')


# Routes
app.add_url_rule('/', 'home', home)
