# Q4_Estrutura sequencial _https://wiki.python.org.br/EstruturaSequencial

i=0
n=0
nota=0.0
soma=0.0
for i in range(0,4):
  if nota >= 0.0 and nota <=10.0:
     nota=float(input('Entre a nota do bimestre:  '))
     soma+=nota
     s=round(soma,2)
     m=s/4
     mr=round(m,2)
     n+=1
     if n==4:
         print('Total das notas = ',s)
         print('A média das notas é ',mr)
          
     
  else:
      print('Nota inválida!')
      break
