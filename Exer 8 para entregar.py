import numpy as np

ano_nascimento = {

}
lista1 = [0.0]*20
sexo = [None]*20
lista3 = [0.0]*20
lista4 = [0]*20
listaAlturaF = []*20
listaAlturaM = []*20
listaNotaF = []*20
listaNotaM = []*20
h = 0
m = 0
x = 0
y = 0
soma = 0

# TRANSFORMANDO EM VETOR
altura = np.array(lista1)
nota = np.array(lista3)
ano = np.array(lista4)


#Ler os valores
for i in range(3):
    altura[i] = float(input("Digite a altura:"))
    nota[i] = float(input("Digite a nota:"))
    sexo[i] = str(input("Digite o seu sexo[M/F]:")).upper()[0]
    if(sexo[i] == 'M'):
        listaAlturaM.append(altura[i])
        listaNotaM.append(nota[i])
        x += 1
    else:
        listaAlturaF.append(altura[i])
        listaNotaF.append(nota[i])
        y += 1
    data = int(input("Digite o ano de nascimento:"))
    if data in ano_nascimento:
        ano_nascimento[data] = ano_nascimento[data] + 1
    else:
        ano_nascimento[data] = 1

#Mostrar quem é o mais alto e mais baixo do grupo
print(f'Menor altura do grupo:{altura.min()}')
print(f'Maior altura do grupo:{altura.max()}')

# FEITO A LEITURA AGORA TRANSFORMA OS DADOS DE CADA GENERO EM VETOR
alturaF = np.array(listaAlturaF)
alturaM = np.array(listaAlturaM)
notaF = np.array(listaNotaF)
notaM = np.array(listaNotaM)
print(f'A altura media das mulheres e de:{alturaF.mean()}')
print(f'A nota media das mulheres e de:{notaF.mean()}')

#Alocar os valores de pedidos a pergunta b e c
for i in range(y):
    if(alturaF[i] > alturaF.mean()):
        m += 1
for i in range(x):
    if(notaM[i] < notaF.mean()):
        h += 1

print(f'A quantidade de mulheres com altura acima da media:{m}')
print(f'A quantidade de homens com nota inferior a media das mulheres:{h}')
    
#Percentual de nascidos

v = int(input("Digite o ano que queria verificar:"))
perce = ano_nascimento[v]/20
print(f"O percentual de nascidos naquele ano e de:{perce * 100}%")