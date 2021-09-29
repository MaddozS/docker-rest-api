from flask import Blueprint, json, jsonify
import functools

bp = Blueprint("alumnos", __name__, url_prefix="/alumnos")

@bp.route('/')
def alumnos():
    alumnos = [
        {"nombre": "Jorge Alameda", "matricula": 15004131},
        {"nombre": "Axel Anaya", "matricula": 15004133 }
    ]
    return json.dumps(alumnos)