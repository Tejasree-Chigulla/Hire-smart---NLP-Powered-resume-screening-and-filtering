import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    SECRET_KEY = "your_secret_key"
    ALLOWED_EXTENSIONS = {"pdf", "docx"}
    
    # ✅ Set maximum upload limit (e.g., 50MB)
    MAX_CONTENT_LENGTH = 120 * 1024 * 1024  # 50MB limit

    @staticmethod
    def allowed_file(filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
