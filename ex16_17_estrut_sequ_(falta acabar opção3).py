# Q16_Estrutura sequencial _https://wiki.python.org.br/EstruturaSequencial
# Calculadora de tinta
print('Bem-vindo à COMERCIAL YAMAMOT! Vamos calcular a quantidade de tinta!\n')
a= float(input('Informe a área(m²) a ser pintada:  '))
l=a/6
lm=l+(l*0.10)
lm1=round(lm,2)
print('Você precisará de ',lm1,'litros de tinta.')

lt=lm/18
ltr=round(lt,0)
ltr2=lt-ltr
#print(lt,ltr,ltr2)
gl=lm/3.6
glr=round(gl,0)
glr2= gl-glr
#print(gl,glr,glr2)

op=int(input('Suas opções:\n'
              '(1) Lata c/ 18 l R$ 80,00\n '
            "(2) Galão c/ 3.6 l R$ 25,00\n"
              "(3) Mix Lata e Galão : "))
if op ==1 :
       if ltr2>0.0 and ltr2<0.99:
        lt=80.0
        ltr2=ltr+1
        ltr2r=round(ltr2,0)
        print('\nQuantidade de latas (18 l);',ltr2r)
        print('Valor total da compra R$',lt*ltr2r)

if op ==2 :
       if ltr2>0.0 and ltr2<0.99:
        gl=25.0
        glr2=glr+1
        glr2r=round(glr2,0)
        print('\nQuantidade de galões (3,6 l);',glr2r)
        print('Valor total da compra R$',gl*glr2)
     
if op ==3:# a lógica aqui não está funcionando, melhorar.
    if lm1%18!=0 and lm1%18 >=0.0 and lm1%18 <0.5:
       lt1=lm1/18
       lt1r=round(lt1,0)
       gl1=lm1%18
       gl2=round(gl1,1)
       print('Quantidade de latas (18 l): ',ltr1r)
       print('Quantidade de galões(3,6 l): ',gl2)
    if lm1%18!=0 and lm1%18 <= 0.5 and lm1%18< 0.99:
           lt1=lm1/18
           lt1r=round(lt1,0)
           gl1=lm1%18
           gl2=round(gl1,1)
           gl3=gl2+1
           print('Quantidade de latas (18 l): ',ltr1r)
           print('Quantidade de galões(3,6 l): ',gl3)
           

