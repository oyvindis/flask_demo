from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from .endpoints import Todo, TodoList

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)