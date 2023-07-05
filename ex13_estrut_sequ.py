# Q13_Estrutura sequencial _https://wiki.python.org.br/EstruturaSequencial
# Peso ideal(homem ou mulher)

s=int(input('Informe seu sexo (1) Masc (2) Fem : '))
if s!=1 and s!=2:
    print('Opção inválida! Tente outra vez.\n')
    exit()

    
alt= float(input('Entre com sua altura em metros: '))
if alt<0.5 or alt>=3.0:
   print('Opção inválida! Tente outra vez.\n')
   exit()
   
 
if s == 1 and alt > 0.5 and alt <= 2.5:
   ps=  (72.7*alt) - 58
   psr=round(ps,2)
   print('Seu peso ideal é ', psr,'Kg.')
   
if s == 2 and alt > 0.5 and alt <= 2.5:
    ps=  (62.1*alt) - 44.7
    psr=round(ps,2)
    print('Seu peso ideal é ', psr,'Kg.')
    
    