#############################################
#          Gomar Salvador Juan Manuel       #
#          Mejía Chávez María Fernanda      #
#############################################

print('#-----Representación de la red semántica en json-------#')
print()
#importamos 
import json
#para abrir nuestro documento json

with open("RSN.json","r") as read_file:
	data = json.load(read_file)
	Conocimiento= data['Conocimiento']
	##print(Conocimiento)

def tiene(A,B,V,Se):
	if not Se:
		return False
	i = 0
	j = len(Se)
	if B == "Vive" or B == "Tiene":
		while i < j:
			if Se[i][0] == A and Se[i][1] == B and Se[i][2] == V:
				return True
			i = i + 1
		else:
			return False
	else:
		while i < j:
			if Se[i][0] == A:
				if Se[i][1] == B:
					if Se[i][2] == V:
						return True
				else:
					A = Se[i][2]
					i = -1
		else:
			return False



#funcion para la base de conocimientos
def valida(A,B,V):
	return tiene(A,B,V,Conocimiento)
	#print('hola')
## GENERAMOS UNA FUNCIÓN **REPL** ##
#(Read-Eval-Print-Loop) --> Bucle Lectura-Evaluación-Impresión #
def main():
	print("Bienvenido")
	print("Puedes consultar escribiendo valida(<Animal>,<Vive>,<Lugar>) ó valida(<Animal>,<Tiene>,<Caracteristica>) ó valida(<Animal>,<Es>,<Cualidad>)")
	Terminar = False
	while not Terminar:
		Leer = input("> ")
		Imprimir = eval(Leer)
		print(Imprimir)
 
if __name__ == "__main__":
	main()
