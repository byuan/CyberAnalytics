from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.getenv('DB_HOST')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_DATABASE=os.getenv('DB_DATABASE')
