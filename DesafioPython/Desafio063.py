n = int(input('Quantos termos de Fibonacci você quer ver? '))
a = 0
b = 1
t = 0
while n != 0:
    print(t, end=' ')
    t = a + b
    a = b
    b = t
    n = n - 1
