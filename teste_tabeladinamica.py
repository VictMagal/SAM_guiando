# identificador = [1,2,3,4,5,6,7]

# total = ['a','b','c','d','e','f','g']

# faturado = ['h','k','c','d','2','f','c']

# dicionario = dict(zip(identificador, total))
# dicionario2 = dict(zip(identificador, faturado))

# print(dicionario)
# print(dicionario2)


# for i in identificador:
#     i-=1
#     if dicionario[identificador[i]] == dicionario2[identificador[i]]:    
#         print(dicionario[identificador[i]])
#     else:
#         print('errado', identificador[i])
#         print('layout')

id_twn = []
lista_id = []

data = '11/12/2021'
conta = str(12342141)

ano = data [6:]
mes = data [3:5]
dia = data [:2]

identificador = conta + '_'+ ano + mes + dia
if identificador in lista_id:
    print('id repetido')
lista_id.append(identificador)

print(identificador)