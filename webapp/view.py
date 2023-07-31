import flask
from flask import request, jsonify
from uuid import uuid4
import json

app = flask.Flask(__name__)

# Create a list to store the todo items
todos = {}

def task_as_id(task):
  return task.lower().replace(' ', '_')

# Define the API endpoints
@app.route('/todos', methods=['GET'])
def get_todos():
  """Get all the todo items."""
  return todos


@app.route('/todos/<task>', methods=['GET'])
def get_todo(task):
  """Get a todo item by its ID."""
  return todos[task_as_id(task)]

@app.route('/todos', methods=['POST'])
def add_todo():
  """Add a todo item."""
  task = request.json['task']
  todos[task_as_id(task)] = {'status': False}
  return {'message': 'Todo item added successfully'}

@app.route('/todos/<task>', methods=['PUT'])
def update_todo(task):
  """Update a todo item."""
  status = request.json['status']
  todos[task_as_id(task)]['status'] = status
  return {'message': 'Todo item updated successfully'}

@app.route('/todos/<task>', methods=['DELETE'])
def delete_todo(task):
  """Delete a todo item."""
  todos.pop(task)
  return {'message': 'Todo item deleted successfully'}

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")