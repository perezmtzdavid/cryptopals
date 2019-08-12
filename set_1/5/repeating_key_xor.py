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

cadena_bytes = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
llave = b"ICE"
plaintext = cifrado(cadena_bytes,llave)
print(plaintext)
