"""
Created on Tue Oct 11 23:32:44 2022
@author: Renso Guimaraes
"""

v = int(input("Informe a quantidade de garrafas vazias no dia (V): "))
e = int(input("Informe a quantidade de garrafas vazias encontradas ao longo do dia (E):"))
b = int(input("Informe a quantidade de garrafas vazias necessárias para a troca por uma cheia (B):"))

if (v < 0) or (e < 0) or (v + e < b) or (b < 2):
    print("Para ocorrer troca: ")
    print("  -> V ou E tem que ser maior que ZERO e não podem ser NEGATIVOS; ")
    print("  -> B tem que ser maior 1; e,")
    print("  -> a soma de V + E tem que ser maior ou igual a B.")
    # observacoes: 
    #  1) se for permitido B=1 vai haver divisão por 1 infinitamente, causando loop infinito
    #  2) não faz sentido o numero de garrafas vazias para troca (V+E) ser menor que o número de cheias para troca (B))
else:    
    vazias = v + e
    cheias = vazias // b # divisao inteira
    sobravazia = vazias % b  # resto da divisao
    parcial = cheias + sobravazia
    novatroca = parcial
    while (novatroca >= b): # enquanto tiver quantidade vazia suficiente para ser trocada
        cheias = novatroca // b
        sobravazia = novatroca % b
        parcial = parcial + cheias # soma a quantidade inteira de garrafas cheias trocadas a parcial
        novatroca = cheias + sobravazia # calcula a nova quantidade para troca
    resultado = parcial  # resultado final  
    print("Resultado = ", resultado)