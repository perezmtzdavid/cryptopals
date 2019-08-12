import base64

def cifrado(cadena_bytes,llave):
    plaintext = ""    
    indice = 0
    len_llave = len(llave)    
    for byte in cadena_bytes:            
        if(indice + 1 == len_llave):               
            plaintext += ''.join('{0:x}'.format(byte ^ llave[indice])).zfill(2)
            indice = 0
        else:
            plaintext += ''.join('{0:x}'.format(byte ^ llave[indice])).zfill(2)
            indice += 1
    return plaintext

llave = b"Terminator X: Bring the noise"
plaintext = ""
with open("encode.enc",'rb') as file:
    cadena_b64 = file.read()
    cadena = base64.b64decode(cadena_b64)
    plaintext = cifrado(cadena,llave)

with open("salida","w") as file_2:
    file_2.write(bytes.fromhex(plaintext).decode('utf-8'))    