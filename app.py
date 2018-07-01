#sk/bin/python
from flask import Flask, jsonify
from flask import url_for
from flask import make_response
from flask import request
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'happiness_title': u'Sanju Movie and Bawarchi lunch',
        'happiness_description': u'Fun to watch Sanju Movie with Family and post that enjoying delete', 
        'happiness_amount': 1400
    },
    {
        'id': 2,
        'happiness_title': u'Visit to Bull Temple',
        'happiness_description': u'Visited with Parents, Awesome place to be for 2 hours, Beautifull Rock garden Near by, Had good food just outside rock garden', 
        'happiness_amount': 1200
    }
]
@app.route('/happiness/events/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

def get_task():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

#post method
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'happiness_title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'happiness_title': request.json['happiness_title'],
        'happiness_description': request.json.get('happiness_description', ""),
        'happiness_amount': request.json['happiness_amount'] 
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'happiness_title' in request.json and type(request.json['happiness_title']) != unicode:
        abort(400)
    if 'happiness_description' in request.json and type(request.json['happiness_description']) is not unicode:
        abort(400)
    if 'happiness_amount' in request.json and type(request.json['happiness_amount']) is not int:
        abort(400)
    task[0]['happiness_title'] = request.json.get('happiness_title', task[0]['happiness_title'])
    task[0]['happiness_description'] = request.json.get('happiness_description', task[0]['happiness_description'])
    task[0]['happiness_amount'] = request.json.get('happiness_amount', task[0]['happiness_amount'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

#@app.errorhandler(404)
#def not_found(error):
#    return make_response(jsonify({'error': 'Not found'}), 404)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
