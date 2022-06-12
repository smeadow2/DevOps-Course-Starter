from flask import Flask
from flask import render_template
from todo_app.data.session_items import get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    to_do_list = get_items()
    return render_template('index.html', to_do_list=to_do_list)