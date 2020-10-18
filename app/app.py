from flask import Flask 

from app.config import config

app = Flask(__name__)

# load the config
app.config.from_object(config["default"])

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))