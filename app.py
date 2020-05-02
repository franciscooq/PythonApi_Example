from flask import Flask, jsonify, request

api = Flask(__name__)

Users = [
    {
        "Name": "Francisco O. Queiroz",
        "Age": 30,
        "Email":"franciscooq@yahoo.com.br"
    }
]

#Metodos
@api.route('/Users',methods=['GET'])
def Home():
    return jsonify(Users), 200


#Garante o Start da aplicação
if  __name__ == '__main__':
    api.run(debug=True)