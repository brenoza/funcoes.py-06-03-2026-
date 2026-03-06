notas = [7.5, 8.0, 9.5, 6.0, 8.5]

print("Notas: ", notas)

print("Menor nota:" min(notas))
print("Menor nota: ", max(notas))
print("Soma: ", sum(notas))
print("Media: ", sum(notas) / len(notas))

nomes = ["Adriana", "Barbaça", "Carla", "Daniel"]

print("Usando FOR simples:")

for nome in nomes:
    print(f"OLá, {nome}")

print("Usando enumerate:")

for indice, nome in enumerate(nome):
    print(f"Posição{indice}: {nome}")

    original = ["A", "B", "C"]
    copia = list(original)
    
    print("Original: ", original)
    print("Cópia: ", copia)
    print("São iguais: ", original == copia)

    copi.append("D")
    print("Original: ", original)
    print("Cópia: ", copia)
    print("São iguais: ", original == copia)
