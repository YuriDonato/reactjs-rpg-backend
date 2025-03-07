import os
import firebase_admin
from firebase_admin import credentials, firestore

# Obtenha o caminho do arquivo de credenciais via variável de ambiente
cred_path = os.getenv("FIREBASE_CREDENTIALS", "caminho/para/serviceAccountKey.json")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
