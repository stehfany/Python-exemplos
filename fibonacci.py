"""
Função que retorna ao usuário se o número digitado é uma sequência de Fibonacci.
"""
def fibonacci(n):

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def pertence_fibonacci(num):
  
    n = 0
    while fibonacci(n) <= num:
        if fibonacci(n) == num:
            return True
        n += 1
    return False


num = int(input("Digite um número: "))

if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")