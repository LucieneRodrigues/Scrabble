'''Cada letra de uma palavra valem um ponto diferente'''
print('Digite duas palavras para saber qual das palavras vale mais.')
from multiprocessing.sharedctypes import Value
palavra1 = str(input('Dgite a palavra 1: ')).strip().upper()
palavra2 = str(input('Dgite a palavra 2: ')).strip().upper()
dados = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,
'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
ponto_palavra1 = 0
for caracter in palavra1:
   key = caracter #pode colocar: caracter.upper() para jogar pra maiúscula
   novo_ponto = dados.get(key,0)
   ponto_palavra1 += novo_ponto
ponto_palavra2 = 0
for caracter in palavra2:
    key = caracter 
    novo_ponto = dados.get(key,0)
    ponto_palavra2 += novo_ponto
palavra1 = palavra1.capitalize()
palavra2 = palavra2.capitalize()
if ponto_palavra1 > ponto_palavra2:
    print(f'A palavra {palavra1}, Vale mais!')
elif ponto_palavra2> ponto_palavra1:
     print(f'A palavra {palavra2}, Vale mais')
else:
    print(f'A palavra {palavra1} vale {ponto_palavra1} pontos e a palavra {palavra2} vale {ponto_palavra2} pontos.')
    print(f'As duas palavras {palavra1} e {palavra2} tem a mesma pontuação.')



