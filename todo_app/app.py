from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session

from operator import itemgetter

from todo_app.data.session_items import add_item
from todo_app.data.session_items import get_items
from todo_app.data.session_items import get_item
from todo_app.data.session_items import remove_item
from todo_app.data.session_items import save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    to_do_list = get_items()

    if session.get('sesh_sort_order') == None:
        session['sesh_sort_order'] = ''
        
    curr_sort_order = session.get('sesh_sort_order')

    if curr_sort_order != '':
        to_do_list = sorted(to_do_list, key=itemgetter('status'), reverse=eval('curr_sort_order == \'Descending\''))

    return render_template('index.html', to_do_list=to_do_list)

@app.route('/add', methods=['POST'])
def add_item_to_list():
    title = request.form.get('to_do_title')

    add_item(title)

    return redirect('/')

@app.route('/sort')
def sort_list():
    curr_sort_order = session.get('sesh_sort_order')
    
    if curr_sort_order == '':
        curr_sort_order = 'Ascending'
    elif curr_sort_order == 'Ascending':
        curr_sort_order = 'Descending'
    elif curr_sort_order == 'Descending':
        curr_sort_order = ''

    session['sesh_sort_order'] = curr_sort_order

    return redirect('/')

@app.route('/complete/<id>', methods=['POST'])
def complete_item(id):
    item = get_item(id)
    item['status'] = "Completed"
    save_item(item)

    return redirect('/')

@app.route('/delete/<id>', methods=['POST'])
def delete_item_from_list(id):
    remove_item(id)

    return redirect('/')