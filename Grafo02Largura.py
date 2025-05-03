'''
Filipe Valle Moreira - RA: 40418944
Gabriel Macedo de Araujo Vieira - RA: 2401585
Samuel Bertozzi Negrão - RA: 2400583
'''
vertice = ["A","B","C","D","E","F"]
arestas = [['A','B'], ['B','C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['A', 'F'], ['A', 'D'], ['C', 'E']]

fila = []
visitados = []
inicio = 'A' 
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
