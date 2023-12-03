from flask_restful import Resource
from flask import jsonify, request, abort
from api.utils.classifier import load_model, classify_image
from api.utils.validators import is_file_allowed
from config.config import config

model = load_model()

class AnalyzeController(Resource):

    def post(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'})
        
        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file provided'})
        elif not is_file_allowed(file.filename):
            return jsonify({'error': 'Only files of type png, jpg and jpeg are allowed'})
        
        try:
            file_path = f'{config.ASSETS_LOCATION}/uploaded_file.jpg'
            file.save(file_path)

            predictions = classify_image(file_path, model)

            return jsonify({'predictions': predictions})
        except Exception as e:
            return abort(400, description="Failed to analyze the uploaded image.")
    
