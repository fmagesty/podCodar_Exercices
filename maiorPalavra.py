# Dada uma lista de palavras, retorne a maior palavra.
# Obs: 
# * Caso tenhamos mais de uma palavra com o número maior de letras, retorne a primeira palavra encontrada
# * Se a lista for vazia, retorne null

# Organize bem o código e escreva os testes que acharem relevante!



palavras = ["paulo", "rafaela", "enzo"]
palavras_2 = ["paulo", "pedro", "ana"]
palavras_3 = []

maiorPalavra = 'a'



for i in palavras:
    if len(i) > len(maiorPalavra):
        maiorPalavra = i


print(maiorPalavra)





