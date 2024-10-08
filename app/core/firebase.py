import firebase_admin
from firebase_admin import credentials, firestore, storage

from app.core.config import settings

cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred, {"storageBucket": settings.FIREBASE_STORAGE_BUCKET})

db = firestore.client()
bucket = storage.bucket()
