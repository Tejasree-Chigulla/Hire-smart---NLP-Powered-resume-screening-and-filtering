from flask import Flask
from modules.routes import main
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# ✅ Set a Secret Key for Flask Session
app.secret_key = "your_secret_key_here"  # 🔑 Change this to a strong secret key

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Register Blueprint
app.register_blueprint(main, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)

