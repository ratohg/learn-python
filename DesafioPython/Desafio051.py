pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = pt + (10 - 1) * r
for c in range(pt, decimo +1, r):
    print(c, end=' ')
