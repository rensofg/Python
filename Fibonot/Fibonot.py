"""
Created on Tue Oct 11 21:38:26 2022
@author: Renso Guimaraes
"""

n = int(input("Qual o n-ésimo número da sequência de Fibonot deseja encontrar: "))
ultimo = 1    # usado na sequencia de fibo
penultimo = 1 # usado na sequencia de fibo

if (n < 1):
    print("Deve-se informar um número maior que ZERO!")
else:
    count = 1 # contagem da sequencia
    while count <= n: # loop da fibo
        fibo = ultimo + penultimo # calcula fibo
        penultimo = ultimo
        ultimo = fibo
        fibonot = penultimo + 1 # calcula fibonot
        while (count <= n) and (fibonot < fibo): # loop da fibonot
            if (count == n):  # controla para impressao apenas n-ésimo número da sequencia
                print(count, "º", " Fibonot = ", fibonot)
            fibonot += 1 # incrementa fibonot enquanto for menor que fibo
            count += 1 # incrementa contagem da sequencia
