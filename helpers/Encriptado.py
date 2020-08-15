from cryptography.fernet import Fernet

class Encriptado():
   
       def Encriptar(self, texto) :
        
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt("212121212")
        return token
    
       def Desencriptar(self, texto):
        key = Fernet.generate_key()
        f = Fernet(key)
        token=  f.decrypt(texto)
        return token
