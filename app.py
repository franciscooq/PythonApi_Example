from flask import Flask, jsonify, request

api = Flask(__name__)

_Users = [
    {
        "id": 1,
        "Name": "Francisco O. Queiroz",
        "Age": 30,
        "Email":"franciscooq@yahoo.com.br"
    }
]

#Methods
@api.route('/Users',methods=['GET'])
def ListUsers():
    return jsonify(_Users), 200

@api.route('/Users/add',methods=['POST'])
def AddUser():
    data = request.get_json()
    _Users.append(data)
    return jsonify(_Users), 201

@api.route('/Users/get/<int:id>',methods=['GET'])
def GetUserById(id):
    for user in _Users:
        if (user['id'] == id):
            return jsonify(user), 200

#Initialize App
if  __name__ == '__main__':
    api.run(debug=True)