import os
import json
from dotenv import load_dotenv

# firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

CONFIG = json.loads(os.getenv('FIREBASE_CONFIG'))
cred = credentials.Certificate(CONFIG)

firebase_admin.initialize_app(cred)

db = firestore.client()
quotes = db.collection('quotes')

load_dotenv()

# this will work for now
# I'll make this script a real boy one day
phrases = []

# add each item in the phrases list
for index, item in enumerate(phrases, start=1):
    print(f'adding {index} of {len(phrases)}')
    quotes.add({
        'value': item
    })