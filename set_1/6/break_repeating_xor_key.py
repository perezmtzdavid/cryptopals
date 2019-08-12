import base64
import heapq

class hamming_distance:
    def hamming_dist(self,cadena_1,cadena_2):
        str_hamming_distance = ""
        count_hamming_distance = 0
        
        if(len(cadena_1) != len(cadena_2)):
            len_faltante = len(cadena_1) - len(cadena_2)
            cadena_2 += b"0" * len_faltante
       
        for index in range(len(cadena_1)):    
            str_hamming_distance +=  ''.join('{0:b}'.format(   cadena_1[index] ^ cadena_2[index]   )) 
        
        for bit in str_hamming_distance:
            if(bit == "1"):
                count_hamming_distance += 1
        
        return count_hamming_distance


dicc_res = {}
bit_cadena_1 = ""
bit_cadena_2 = ""

ham_dist = hamming_distance()

with open("encode.enc","r") as file:
    data = file.read()

file_decode = base64.b64decode(data)
len_file_decoded = len(file_decode)
hamming_distance_lowest = 1000000000


dicc_res_sorted = []

for KEYSIZE in range(2,41):
    for index in range(0,len_file_decoded - KEYSIZE,KEYSIZE):       
        hamming_distance_norm = ham_dist.hamming_dist(file_decode[index:index+KEYSIZE],file_decode[index + KEYSIZE:index + 2*KEYSIZE])/KEYSIZE                
        if(hamming_distance_norm < hamming_distance_lowest):
            if(hamming_distance_norm != 0):                
                dicc_res.update([(KEYSIZE,hamming_distance_norm)])        
                hamming_distance_lowest = hamming_distance_norm
    hamming_distance_lowest = 10000

for i in range(2,41):
    heapq.heappush(dicc_res_sorted,(dicc_res[i],i))    

dicc_res_sorted = heapq.nsmallest(40,dicc_res_sorted)
for i in dicc_res_sorted:
    print(i)
