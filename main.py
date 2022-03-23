import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import functions_framework

cred = credentials.Certificate('aiprojectmanagementtool-firebase-adminsdk-40a4k-cbb0135626.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

@functions_framework.http
def get_data(request):
    users_ref = db.collection(u'projects')
    docs = users_ref.stream()
    for doc in docs:
        data = doc.to_dict()
    return data
