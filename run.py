import os
from dotenv import load_dotenv

from app import create_app, db
from app.config import basedir
from models import User, Post

load_dotenv(os.path.join(basedir, '.env'))

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
