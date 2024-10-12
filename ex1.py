def fibonacci(valor):
    n1, n2 = 0, 1
    sequencia = [n1,n2]

    while n2 < valor:
        proximo = n1+n2 
        sequencia.append(proximo)
        n1,n2 = n2, proximo
    return sequencia
    
num = int(input("Digite um número: "))
sequencia = fibonacci(num)

if num in sequencia:
    print(f"Número {num} pertence a sequencia de Fibonacci")
else: 
    print(f"Número {num} não pertence a sequencia de Fibonacci")
    

