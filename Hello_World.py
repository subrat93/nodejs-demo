from flask import Flask
import os
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=port)