#############################################
#          Gomar Salvador Juan Manuel       #
#          Mejía Chávez María Fernanda      #
#############################################


print('#-----Representación de Tweet-------#')
print()
#importamos 
import json
#para abrir nuestro documento json

with open("Emuestral.json","r") as read_file:
	data = json.load(read_file)
	Conocimiento= data['Probabilidades']
##print(Conocimiento)

import json
#para abrir nuestro archivo
archivo = open ('tweet.txt','r')
ar = archivo.read()
tw = ar.split()
archivo.close()

def stream(tex, CES):
    suma = 0
    prom = 0
    l = len(tex)
    l1 = len(CES)
    comparacion = []
    for i in range(l):
        for j in range (l1):
            if CES[j][0] == tw[i]:
                comparacion.append(CES[j])
        for l in range(len(comparacion)):
            suma += float(comparacion[l][1])
            prom = suma / len(comparacion)
        if (prom > .55):
            return "Stream"
        else:
            return "No es stream"

print(stream(tw, Conocimiento))

