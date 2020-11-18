from cryptography.fernet import Fernet, InvalidToken

class EncryptedKey:
    def __init__(self, chat_id, url, nickname, password, next_action):
        self._chat_id = chat_id
        self._id = url
        self.nickname = nickname
        self.passwod = password
        self.next_action = next_action

    def create_key(self):
        key = Fernet.generate_key()
        return key

  
    
    def encrypted_key(self, key):
        fernet = Fernet(key)
        encrypted = fernet.encrypt(self.password.encode())
        return encrypted


    def get_key(self, encrypted):
        decrypted = Fernet.decrypt(encrypted)
        return decrypted.decode() # real password

def get_EncryptedKey_from_dict(EncryptedKey_dict):
    e = EncryptedKey(EncryptedKey_dict["chat_id"], EncryptedKey_dict["_id"], EncryptedKey_dict["nickname"], EncryptedKey_dict["passwod"], EncryptedKey_dict["next_action"])
    return e

