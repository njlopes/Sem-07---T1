d1 = int(input(""))
m1 = int(input(""))
a1 = int(input(""))

d2 = int(input(""))
m2 = int(input(""))
a2 = int(input(""))
 
if a1>a2 or (a1==a2 and m1>m2) or (a1==a2 and m1==m2 and d1>d2):
     print('{}/{}/{}'.format(d1, m1, a1))
else:
     print('{}/{}/{}'.format(d2, m2, a2))
