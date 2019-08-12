from Crypto.Cipher import AES
from base64 import b64decode

with open("b64.enc","rb") as file:
    key = b"YELLOW SUBMARINE"
    data = file.read()
    b64_decode = b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)    	
    with open("output","w") as output:
        output.write(cipher.decrypt(b64_decode).decode("utf-8"))
