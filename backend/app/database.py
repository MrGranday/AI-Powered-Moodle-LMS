from pymongo import MongoClient
from .config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

# Collections
user_collection = db["users"]
course_collection = db["courses"]
lesson_collection = db["lessons"]
progress_collection = db["progress"]

def get_db():
    return db
