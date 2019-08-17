
cadena_1_hex = "1c0111001f010100061a024b53535009181c"
cadena_2_hex = "686974207468652062756c6c277320657965"
long_cadena = len(cadena_1_hex)
a = ''
for i in range(0,long_cadena):
    res = int(cadena_1_hex[i],16)  ^ int(cadena_2_hex[i],16)   
    a += ''.join('{0:x}'.format(res))
print(a)

