def calc_idade(a,b,c,x,y,z):
   if a == x and b == y:
      return print(c-z)
   elif x>a and b == y:
      return print(c-z-1)
   elif b<y:
      return print(c-z-1)
   else:
      return print (c-z)


def main():
   dia = int(input('Digite o dia atual:'))
   mes = int(input('Digite o mês atual:'))
   ano = int(input('Digite o ano atual:'))

   data_nas = int(input('Digite o dia do seu nascimento:'))
   mes_nas = int(input('Digite o mês do seu nascimento:'))
   ano_nas = int(input('Digite o ano do seu nascimento:'))

   data = calc_idade(dia,mes,ano,data_nas,mes_nas,ano_nas)


if __name__ =='__main__':
   main()
