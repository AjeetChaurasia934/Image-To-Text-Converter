from flask import Flask

app=Flask(__name__)

from i2twebapp import routes
from i2twebapp import templates