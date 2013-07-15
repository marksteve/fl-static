from flask import Flask
from fl_static import Shock, Jinja2Magic


def create_app():
    return Flask(__name__)


jinja2_magic = Jinja2Magic(color='blue')
app = Shock(create_app(), root='data', magics=[jinja2_magic]).run(debug=True)
