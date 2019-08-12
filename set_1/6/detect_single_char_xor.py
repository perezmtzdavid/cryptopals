import heapq
from spellchecker import SpellChecker
import base64
from array import *

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
        "z": 	0.074, 
        "A": 	8.167,
        "B": 	1.492, 	 
        "C": 	2.782, 	 
        "D":	4.253, 	 
        "E": 	12.702, 	 
        "F": 	2.228, 	 
        "G": 	2.015, 	 
        "H": 	6.094, 	 
        "I": 	6.966, 	 
        "J": 	0.153, 	 
        "K": 	0.772, 	
        "L": 	4.025, 	
        "M": 	2.406, 	
        "N": 	6.749, 	 
        "O": 	7.507, 	
        "P": 	1.929, 	
        "Q": 	0.095, 	
        "R": 	5.987, 	
        "S": 	6.327, 	
        "T": 	9.056, 	
        "U": 	2.758, 	
        "V":    0.978, 	
        "W": 	2.360, 	
        "X": 	0.150, 	
        "Y": 	1.974, 	
        "Z": 	0.074 
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
    def __init__(self, strings):
        self.strings = strings        
        
    def xor_strings(self):
        puntaje_final_strings = []
        spell = SpellChecker()
        letter_pos = 0
        for line in self.strings:                               
            cadena = line                                               
            res = ''
            puntaje_final = 0
            puntaje_final = []
            for i in range(256):
                #print(cadena)
                for j in cadena:
                    res_byte = ord(j) ^ i                                            
                    res += chr(res_byte)                     
                puntaje_actual = analiza_frecuencia(res) 
                puntaje_final.append((puntaje_actual,res,i,letter_pos))                                                    
                res = ''
            letter_pos += 1
            #print(puntaje_final)            
            ult = heapq.nlargest(1,puntaje_final)          
            puntaje_final_strings.append(heapq.nlargest(2,puntaje_final))  
            #print(ult)
        # #print(puntaje_final_strings)
        # for i in puntaje_final_strings:
        #     print(i)

        for mi in puntaje_final_strings:
            print(mi)
        
        string = ""
        for i in puntaje_final_strings:
            string += chr(i[0][2])
            print(i[0][2])

        print(string)
       
        # for i in puntaje_final_strings:
        #     for stuff in i:
        #         print(stuff)
       
            

            #for i in range(29):
             #   print(ult[i][3])
            
           

        #     puntaje_actual = 0            
        #     for i in range(10):
        #         palabras = ult[i][1].split(' ')
        #         mejor_palabra = spell.known(palabras)
        #         if(mejor_palabra):                       
        #             for palabra in mejor_palabra:
        #                 puntaje_actual += spell.word_probability(palabra)
        #             puntaje_final_strings.append((puntaje_actual,ult[i][1],ult[i][2]))                                                
                          
        # ult = heapq.nlargest(1,puntaje_final_strings)
        # print(ult[0][1])        


