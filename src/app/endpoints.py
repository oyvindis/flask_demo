from typing import Any
from flask_restful import reqparse, abort, Resource


TODOS = {
    'todo1': {'task': 'Lage et API'},
    'todo2': {'task': 'Lage frontend med React'},
    'todo3': {'task': 'Ta i bruk api-et i frontend'}
}


parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, todo_id) -> Any:
        return TODOS[todo_id]

    def delete(self, todo_id) -> Any:
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id) -> Any:
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self) -> Any:
        return TODOS

    def post(self) -> Any:
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201