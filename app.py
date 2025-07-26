from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine


app = Flask(__name__)
api = Api(app)
db = MongoEngine()

app.config["MONGODB_SETTINGS"] = [
    {
        "db": "users",
        "host": "mongodb",
        "port": 27017,
        "username": "root",
        "password": "123abc"
    }
]
db.init_app(app)


class user_model(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.StringField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


class get_users(Resource):
    def get(self):
        return jsonify(user_model.objects())


api.add_resource(get_users, '/users')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
