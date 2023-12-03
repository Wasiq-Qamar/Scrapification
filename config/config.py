class Config(object):
    ASSETS_LOCATION = 'assets'
    MODEL_URL = 'https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4'
    PREDICTION_CLASSES = 'assets/imagenet_class_index.json'
    ALLOWED_FILES = ['png', 'jpg', 'jpeg']

config = Config()