from config import firebaseConfig
from firebase import Firebase

firebase = Firebase(firebaseConfig)
storage = firebase.storage()

def upload_file(file_path, file_name):
    storage.child(f"files/{file_name}").put(file_path)


def dawnload_file(file_name):
    storage.child(f"files/{file_name}").download(file_name)

def get_url(file):
    return storage.child(f"files/{file}").get_url()


