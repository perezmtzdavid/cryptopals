import heapq
from spellchecker import SpellChecker

def analiza_frecuencia(cadena):
    diccionario = {
        "a": 	8.167,
        "b": 	1.492, 	 
        "c": 	2.782, 	 
        "d":	4.253, 	 
        "e": 	12.702, 	 
        "f": 	2.228, 	 
        "g": 	2.015, 	 
        "h": 	6.094, 	 
        "i": 	6.966, 	 
        "j": 	0.153, 	 
        "k": 	0.772, 	
        "l": 	4.025, 	
        "m": 	2.406, 	
        "n": 	6.749, 	 
        "o": 	7.507, 	
        "p": 	1.929, 	
        "q": 	0.095, 	
        "r": 	5.987, 	
        "s": 	6.327, 	
        "t": 	9.056, 	
        "u": 	2.758, 	
        "v":    0.978, 	
        "w": 	2.360, 	
        "x": 	0.150, 	
        "y": 	1.974, 	
        "z": 	0.074 
    }    
    puntaje_final = 0
    for i in cadena:
        val_frecuencia = diccionario.get(i)
        if(val_frecuencia == None):
            val_frecuencia = 0
        else:
            puntaje_final += val_frecuencia        
    return puntaje_final


class cp4_crypt:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def xor_strings(self):
        puntaje_final_strings = []
        file_read = open(self.file_name,"r")
        out = open("salida","w")
        spell = SpellChecker()
        for line in file_read:       
            #print(line) 
            cadena_hex = line.rstrip("\n")     
            cadena = cadena_hex.decode("hex")    
            print(cadena)                               
            res = ''
            puntaje_final = 0
            puntaje_final = []
            for i in range(256):
                for j in cadena:
                    res_byte = ord(j) ^ i
                    res += chr(res_byte) 
                puntaje_actual = analiza_frecuencia(res) 
                puntaje_final.append((puntaje_actual,res,i))
                res = ''
            ult = heapq.nlargest(10,puntaje_final)

            puntaje_actual = 0            
            for i in range(10):
                palabras = ult[i][1].split(' ')
                mejor_palabra = spell.known(palabras)
                if(mejor_palabra):                       
                    for palabra in mejor_palabra:
                        puntaje_actual += spell.word_probability(palabra)
                    puntaje_final_strings.append((puntaje_actual,ult[i][1],ult[i][2]))                                                
                          
        ult = heapq.nlargest(1,puntaje_final_strings)
        print(ult[0][1])
        file_read.close()
        out.close()


