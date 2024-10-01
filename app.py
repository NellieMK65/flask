from flask import Flask, request

# create flask instance
app = Flask(__name__)

# / stands for index/home route
@app.route('/', methods = ['GET', 'POST'])
def index():
    # route logic
    return { "message": "Hello world" }, 401

@app.get('/about')
def about():

    return { "message": "Learning flask" }

@app.post('/about')
def create_about():
    return { "message": "About created" }, 201

"""
->resource related to users

GET /users -> returns a list
POST /users -> create a single user
GET/PATCH/PUT/DELETE -> /users/<id>
"""

class User:
    pass

@app.get("/users")
def users():
    return []

@app.post('/users')
def create_user():
    return { "message": "User created successfully" }, 201

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        user = User.query.filter_by(id = id).first()

        if user == None:
            return {
                "message": "User not found"
            }, 404

        return {
            "id": id,
            "name": "Jane Doe"
        }
    elif request.method == 'PATCH':
        return { "message": f"User {id} updated successfully" }
