# Faça uma função que, dada uma lista contendo sequências de caracteres,  retorne esta mesma sequência ao contrário.

# Exemplo:

# - Entrada: ovo
# - Saída: ovo

# - Entrada: banana
# - Saída: ananab

# Entradas e saídas:

# Você deve escrever uma função que receba uma lista contendo sequências de caracteres ["ola", "ovo", ...]

# Esta função deverá retornar uma lista contendo as mesmas sequências na mesma ordem porém invertidas: ["alo", "ovo", ...]

# Faça uma função que, dada uma lista contendo sequências de caracteres,  retorne True ou False caso a sequência de caracteres seja um Palíndromo.
# entradas_teste = ["Ovo", "bolovo", "banana", "Boneca", "aba"]

lista = ["Ovo", "bolovo", "banana", "Boneca", "aba"]
invertedLista = []
palindromeLista = []

# Invert each word in lista:
def wordInverter():
    for i in lista:
        i = i[::-1]
        invertedLista.append(i)
    print(invertedLista)

# Check for palindromes in lista:
def palCheck():
    for i in lista:
        i = i.lower()
        if i[0] == i[-1] and i[1] == i[-2] and i[2] == i[-3]:
            i = True
        else:
            i = False
        print(i)


wordInverter()
palCheck()
