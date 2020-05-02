from flask import Flask, jsonify, request

api = Flask(__name__)

Users = [
    {
        "Name": "Francisco O. Queiroz",
        "Age": 30,
        "Email":"franciscooq@yahoo.com.br"
    }
]

#Methods
@api.route('/Users',methods=['GET'])
def Home():
    return jsonify(Users), 200


#Inicializa Aplicação
if  __name__ == '__main__':
    api.run(debug=True)