import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import json
from config.config import config

def load_model():
    model_url = config.MODEL_URL
    model = tf.keras.Sequential([hub.KerasLayer(model_url)])
    return model

def decode_predictions_custom(preds, top=5, class_list_path=config.PREDICTION_CLASSES):
    # Load the class labels
    with open(class_list_path, 'r') as f:
        class_list = json.load(f)

    top_indices = np.argsort(preds)[::-1][:top]

    decoded_predictions = []
    for i in top_indices:
        class_id, class_name = class_list[str(i)]
        decoded_predictions.append((class_id, class_name, preds[i]))

    return decoded_predictions

def classify_image(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    predictions = model.predict(img_array)
    predictions = np.squeeze(predictions)

    decoded_predictions = decode_predictions_custom(predictions, top = 3)
    results = []
    for i, (_, label, score) in enumerate(decoded_predictions):
        results.append({'index': i, 'label': label, 'score': float(score)})

    return results
