from config.config import config

def is_file_allowed(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.ALLOWED_FILES