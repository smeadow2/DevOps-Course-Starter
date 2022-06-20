from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from todo_app.data.session_items import get_items
from todo_app.data.session_items import get_item
from todo_app.data.session_items import add_item
from todo_app.data.session_items import sort_items
from todo_app.data.session_items import remove_item
from todo_app.data.session_items import save_item
from todo_app.flask_config import Config
import sys


app = Flask(__name__)
app.config.from_object(Config())

current_sort_reverse = True

@app.route('/')
def index():
    to_do_list = get_items()
    return render_template('index.html', to_do_list=to_do_list)

@app.route('/add', methods=['POST'])
def add_item_to_list():
    title = request.form.get('to_do_title')
    add_item(title)
    return redirect('/')

@app.route('/sort')
def sort_list():
    sort_items(current_sort_reverse)

    return redirect('/')

@app.route('/complete/<id>')
def complete_item(id):
    item = get_item(id)
    item['status'] = "Completed"
    save_item(item)

    return redirect('/')

@app.route('/delete/<id>')
def delete_item_from_list(id):
    remove_item(id)

    return redirect('/')