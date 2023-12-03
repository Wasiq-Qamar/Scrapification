from flask.wrappers import Response
from flask_restful import Resource
from flask import jsonify

class BaseController(Resource):
    response: dict = {
        "response": "application is running",
    }

    def get(self):
        res: Response = jsonify(self.response)
        return res
    
