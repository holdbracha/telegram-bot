from cryptography.fernet import Fernet, InvalidToken

class EncryptedKey:
    def __init__(self, chat_id, url = None, nickname = None, password = None, next_action = None):
        self.chat_id = chat_id
        self.url = url
        self.nickname = nickname
        self.password = password
        self.next_action = next_action

    def create_key(self):
        key = Fernet.generate_key()
        return key

    def update_encrypted_key(self, prop, value):
        self.__dict__[prop] = value

    def encrypted_key(self, key):
        fernet = Fernet(key)
        encrypted = fernet.encrypt(self.password.encode())
        return encrypted


    def get_key_by_decrypted(self, encrypted, key):
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted)
        return decrypted.decode() # real password

def get_EncryptedKey_from_dict(EncryptedKey_dict):
    e = EncryptedKey(EncryptedKey_dict["chat_id"], EncryptedKey_dict["url"], EncryptedKey_dict["nickname"], EncryptedKey_dict["password"], EncryptedKey_dict["next_action"])
    return e

