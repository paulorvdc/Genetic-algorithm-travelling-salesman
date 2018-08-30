from random import shuffle
from random import randint

def codificaCromossomo():
	cromosso = [1,2,3,4,5,6,7,8,9]
	shuffle(cromosso)
	return cromosso

def iniciaPopulacao():
	populacao = []
	for i in range(0,50):
		populacao.append(codificaCromossomo())
	return populacao

def fitness(c):
	f = 0
	for i in range(len(c)-1):
		if i == 0:
			f += grafo[0][c[i]]
			f += grafo[c[i]][c[i+1]]
		else:
			f += grafo[c[i]][c[i+1]]
		if i == 7:
			f += grafo[c[i+1]][0]
	return f

def selecao(p):
	elite = [p[0]]
	roleta = []
	for i in range(1,len(p)):
		if fitness(p[i]) < fitness(elite[0]):
			elite.insert(0,p[i])
			if (len(elite) > 5):
				elite.pop()
		else:
			roleta.append(p[i])
	shuffle(roleta)
	print('Elite:',elite[0],' = ',fitness(elite[0]), 'km')
	p = elite + roleta
	for i in range(25,len(p)):
		p.pop()
	return p

def reproducao(c1,c2):
	divisao = randint(1,7)
	f1 = []
	f2 = []
	for i in range(0,divisao):
		f1.append(c2[i])
		f2.append(c1[i])
	for j in range(divisao,len(c1)):
		f1.append(c1[j])
		f2.append(c2[j])
	if (isCidadeRepetida(f1)):
		f1 = codificaCromossomo()
	if (isCidadeRepetida(f2)):
		f2 = codificaCromossomo()
	return f1 if fitness(f1) < fitness(f2) else f2

def isCidadeRepetida(c):
	if (len(c) > len(set(c))):
		return True
	return False  

def renovaPopulacao(p):
	for i in range(0,25):
		p.append(reproducao(p[i],p[i+1]))
		i += 1
	return p

def printCaminho(c):
	for i in range(len(c)-1):
		if i == 0:
			print(dicionario[0], ' => ', dicionario[c[i]], ' = ', grafo[0][c[i]], ' km')
			print(dicionario[c[i]], ' => ', dicionario[c[i+1]], ' = ', grafo[c[i]][c[i+1]], ' km')
		else:
			print(dicionario[c[i]], ' => ', dicionario[c[i+1]], ' = ', grafo[c[i]][c[i+1]], ' km')
		if i == 7:
			print(dicionario[c[i+1]], ' => ', dicionario[0], ' = ', grafo[c[i+1]][0], ' km')

def printGrafo():
	for i in range(len(grafo)):
		print()
		for j in range(len(grafo[i])):
			if grafo[i][j] != 0:
				print(dicionario[i], ' => ', dicionario[j], ' = ', grafo[i][j], ' km')

dicionario = {0: "Guarapuava", 1: "Curitiba", 2: "Ponta Grossa", 3: "Londrina", 4: "Maringá",
			  5: "Umuarama", 6: "Toledo", 7: "Cascavel", 8: "Francisco Beltrão", 9: "Pato Branco"}

grafo = [[  0,258,164,441,294,458,289,240,217,186],
		 [258,  0,117,394,431,595,547,498,243,457],
		 [164,117,  0,277,314,478,453,404,381,350],
		 [441,394,277,  0, 97,261,415,366,551,608],
		 [294,431,314, 97,  0,164,295,269,454,480],
		 [458,595,478,261,164,  0,131,180,365,422],
		 [289,547,453,415,295,131,  0, 49,234,291],
		 [240,498,404,366,269,180, 49,  0,185,242],
		 [217,243,381,551,454,365,234,185,  0, 57],
		 [186,457,350,608,480,422,291,242, 57,  0]]

p = iniciaPopulacao()

for i in range(0,100):
	p = selecao(p)
	p = renovaPopulacao(p)

print('Caminho:')
printCaminho(p[0])