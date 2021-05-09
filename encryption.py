import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "uTCtdl1MieFX!dY$$LiXa2g$Va4Gi&LUbG!Lu@gn" # Replace This String Value With Whatever You Want (Or Just Keep It As It Is)
password = password_provided.encode()
salt = b'\xc3\xd0\x04\xa3\xa5\xa5\x1e\xf5\xd3)\x1b\xf8u\xed\t\x80'
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
key = base64.urlsafe_b64encode(kdf.derive(password))
fernet = Fernet(key)

fot = input("File Or Text [f/t] ")

if fot == "T" or fot == "t":
    mode = input("Encrypt Or Decrypt [e/d] ")
    
    if mode == "E" or mode == "e":    
        data = input("Enter Text To Encrypt: ").encode()
        encrypted = fernet.encrypt(data)
        print(encrypted.decode())
    
    elif mode == "D" or mode == "d":
        data = input("Enter Text To Decrypt: ").encode()
        decrypted = fernet.decrypt(data)
        print(decrypted.decode())

elif fot == "F" or fot == "f":
    mode = input("Encrypt Or Decrypt [e/d] ")
    
    if mode == "E" or mode == "e":    
        input_file = input("Enter Name Of File To Encrypt (With Extension): ")
        output_file = input("Enter Name Of Output File (With Extension): ") 
        
        with open(input_file, 'rb') as f:
            data = f.read()  
        
        encrypted = fernet.encrypt(data)
        
        with open(output_file, 'wb') as f:
             f.write(encrypted)
    
    elif mode == "D" or mode == "d":
        input_file = input("Enter Name Of File To Decrypt (With Extension): ")
        output_file = input("Enter Name Of Output File (With Extension): ")
        
        with open(input_file, 'rb') as f:
            data = f.read()

        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)