'''
Filipe Valle Moreira - RA: 40418944
Gabriel Macedo de Araujo Vieira - RA: 2401585
Samuel Bertozzi Negrão - RA: 2400583
'''
vertice = ["A","B","C","D","E","F"]
arestas = [['A','B'], ['B','C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['A', 'F'], ['A', 'D'], ['C', 'E']]

pilha = []
visitados = []
inicio = 'A'  
pilha.append(inicio)
while pilha:
    print("Pilha atual:", pilha)  
    atual = pilha.pop()  
    if atual not in visitados:
        print("Visitando:", atual)
        visitados.append(atual)
        for origem, destino in arestas:
            if origem == atual and destino not in visitados:
                pilha.append(destino)
print("\nOrdem final de visita:", visitados)
