import base64
cadena_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
cadena = cadena_hex.decode("hex")
print(cadena)
cadena_b64 = base64.b64encode(cadena)
print(cadena_b64)
