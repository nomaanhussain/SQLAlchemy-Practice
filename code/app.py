from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate , identity
from resourses.user import UserRegister
from resourses.item import Item , ListItems


app = Flask(__name__)
app.secret_key = 'noman'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ListItems, '/items')
api.add_resource(UserRegister, '/register')
if __name__ == '__main__':
    app.run(port=5000, debug=True)