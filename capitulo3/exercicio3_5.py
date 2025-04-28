# Calcule o resultado da expressão A > B and C or D, utilizando
# os valores da tabela a seguir.
# A       B       C        D
# 1       2      True     False
# 10      3      False    False
# 5       1      True     True

a1 = 1
a10 = 10
a5 = 5
b2 = 2
b3 = 3
b1 = 1
c1 = True
c0 = False
d1 = True
d0 = False

if a1 > b2 and c1 or d0:
    print("1. True")
else: 
    print("1. False")
if a10 > b3 and c0 or d0:
    print("2. True")
else:
    print("2. False")
if a5 > b1 and c1 or d1:
    print("3. True")
else:
    print("3. False")
