from detect_single_char_xor import cp4_crypt
import base64

with open("encode.enc","r") as file:
    text = file.read()
    text = base64.b64decode(text)
    key_count = 29    
    res_str = ""
    res_str_arr = []

    for i in range(0,key_count):
        for j in range(i,len(text),key_count):
            res_str += chr(text[j])
        #print(res_str)
        res_str_arr.append(res_str)
        #print("--------------------------------------------------------------------")
        res_str = ""
    
    # test = []
    # string = ''
    # for cadena in res_str_arr:
    #     for byte in cadena:
    #         res = ord(byte) ^ 84
    #         string += chr(res)
    #     test.append(string)
    # print(test[0])


test = cp4_crypt(res_str_arr)
test.xor_strings()