def maior (a,s,d,f,g):
    if a>s and a>d and a>f and a>g:
        return a
    if s>d and s>f and s>g:
        return s
    if d>f and d>g:
        return d
    if f>g:
        return f
    else:
        return g


def menor(a,s,d,f,g):
    if a<s and a<d and a<f and a<g:
        return a
    if s<d and s<f and s<g:
        return s
    if d<f and d<g:
        return d
    if f<g:
        return f
    else:
        return g

n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))
n4=int(input('Digite um número:'))
n5=int(input('Digite um número:'))
r=maior(n1,n2,n3,n4,n5)
re=menor(n1,n2,n3,n4,n5)
print(f'O maior número é {r}')
print(f'O menor número é {re}')
