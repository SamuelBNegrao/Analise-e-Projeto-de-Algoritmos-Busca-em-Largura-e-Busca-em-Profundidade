'''
Filipe Valle Moreira - RA: 40418944
Samuel Bertozzi Negrão - RA: 2400583
'''
vertice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arestas = [[0,1], [1,2], [2,3], [2,5], [2,4], [2,6], [3,5], [3,6], [3,4], [4,5], [4,6], [6,5], [6,8], [8,9], [9,7], [9,10], [7,10]]

fila = []
visitados = []
inicio = 0  
fila.append(inicio)
visitados.append(inicio)
while fila:
    print("Fila atual:", fila) 
    atual = fila.pop(0) 
    print("Visitando:", atual)
    for origem, destino in arestas:
        if origem == atual and destino not in visitados:
            fila.append(destino)
            visitados.append(destino)
print("\nOrdem final de visita:", visitados)
