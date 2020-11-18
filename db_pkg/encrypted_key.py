from cryptography.fernet import Fernet
from cryptography.fernet import Fernet, InvalidToken

class EncryptedKey:
    def __init__(self, chat_id, url, nickname, password, next_action):
        self._chat_id = chat_id
        self._id = url
        self.nickname = nickname
        key = Fernet.generate_key()
        fernet = Fernet(key)
        self.encrypted = fernet.encrypt(password.encode())
        self.next_action = next_action

    def get_key(self, chat_id, nickname, password):
        decrypted = fernet.decrypt(self.encrypted)
        print("decrypted: ", decrypted.decode())

def get_sent_from_dict(EncryptedKey):
    pass