nome_completo = input('\033[34mDiga seu nome completo: ').strip()
a = nome_completo.split()
print('\033[32mPrimeiro nome: {}'.format(a[0]))
b = nome_completo.rsplit()
c = nome_completo.rfind(' ')
print('\033[35mUltimo nome: {}'.format(nome_completo[c:].strip()))
