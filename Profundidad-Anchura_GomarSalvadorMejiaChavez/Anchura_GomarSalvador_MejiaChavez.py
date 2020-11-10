#############################################
#          Gomar Salvador Juan Manuel       #
#          Mejía Chávez María Fernanda      #
#############################################

print('#----- A N C H U R A -------#')
print()
#importamos 
import json
with open('Conocimiento-PA.json') as file:
	Conocimiento =json.load(file)
	##print(Conocimiento)

concluidos =[]
guia=[]
otro = []
nextNodo=[]

def priAnchura(Rama,Hoja):
	
	if Rama == Hoja:
		return Hoja
	if nextNodo:
		contador = 0
		for X in nextNodo:
			 contador += 1
		if contador > 1:
			print("Nodo principal: " +nextNodo[0])
			nextNodo.pop(0)
	if otro:
		del otro[:]
	for i in Conocimiento:
		if i[0] == Rama:
			nextNodo.append(i[1])
			otro.append(i[0])
			if i[1] == Hoja:
				nodo = priAnchura(i[1],Hoja)
				return nodo
	concluidos.append(list(set(otro)))
	if concluidos:
		print("Nodos Recorridos")
		print(str(concluidos))
		print(nextNodo[0])
		guia.append(nextNodo[0])
		return priAnchura(nextNodo[0],Hoja)

nodo = priAnchura("10","30")
print("Hijo encontrado - nodo principal: " +nodo)
cam = []
if nodo:
	for c in guia:
		if c not in cam:
			cam.append(c)
	print("Padres(Nodos Revisados)")
	print(cam)
else:
	print("No se encontro")
