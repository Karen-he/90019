from flask import Flask
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)


class TodoSimple(Resource):
    def get(self, todo_id):
        try:
            fo = open("./data/" + todo_id, "r+")
            content = fo.read()
            j = json.loads(content)
            return j
        except:
            return "wrong resource name"

api.add_resource(TodoSimple, '/api/<string:todo_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
