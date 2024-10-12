def quantidade_a(frase):
    letras = "aáàâãAÁÀÂÃ"
    total = 0
    for letra in frase:
        if letra in letras:
            total +=1
    return total

frase = input("Digite uma frase:")
total = quantidade_a(frase)
print(f"A quantidade de 'a's na frase é: {total}")
