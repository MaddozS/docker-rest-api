from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Para obtener a los alumnos, utilice el endpoint /alumnos'

@app.route('/alumnos')
def alumnos():
    alumnos = [
        {"nombre": "Jorge Alameda", "matricula": 15004131},
        {"nombre": "Axel Anaya", "matricula": 15004133 }
    ]
    return jsonify(alumnos)

if __name__ == '__main__':
    app.run(host='0.0.0.0')