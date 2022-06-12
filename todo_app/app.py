from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    to_do_list = get_items()
    return render_template('index.html', to_do_list=to_do_list)

@app.route('/', methods=['POST'])
def add_item_to_list():
    title = request.form.get('to_do_title')
    add_item(title)
    return redirect('/')