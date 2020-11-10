#############################################
#          Gomar Salvador Juan Manuel       #
#          Mejía Chávez María Fernanda      #
#############################################

print('#----- P R O F U N D I D A D-------#')
print()
#importamos 
import json
with open('Conocimiento-PA.json') as file:
	Conocimiento =json.load(file)
way=[]

def profundidad(inicio,busq):
	
	if inicio == busq:
		return busq
		
	for j in Conocimiento:
		if j[0] == inicio:
			way.append(inicio)
			print(j[0])
			resultado=profundidad(j[1],busq)
			if resultado:
				return resultado
	way.pop()
	
resultado=profundidad("10","30")
if resultado:
	print ("Archivo encontrado")
	print(way)
else:
	print("no encontrado")
