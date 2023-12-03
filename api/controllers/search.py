from flask_restful import Resource
from flask import jsonify, request
from api.utils.crawler import find_images, download_image
from api.utils.classifier import load_model, classify_image
from config.config import config

model = load_model()

class SearchController(Resource):

    def get(self):
        keyword = request.args.get('keyword')
        num_images = 5

        images = find_images(keyword, num_images)

        results = []
        for index, image_url in enumerate(images):
            file_name = f'{config.ASSETS_LOCATION}/Image{index}.jpg'

            download_image(image_url, file_name)

            predictions = classify_image(file_name, model)

            results.append({'image': image_url, 'predictions': predictions})

        return jsonify({'data': results})
    
