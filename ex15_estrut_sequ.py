# Q15_Estrutura sequencial _https://wiki.python.org.br/EstruturaSequencial
# contra-cheque
ent1= float(input('Entre o valor da sua hora trabahada:  '))
ent2= float(input('Entre as horas trabalhadas/mês: '))
sl=ent1*ent2
slr=round(sl,3)
print('Salário bruto neste mês é de R$',slr)
ir=sl*0.11
irr=round(ir,2)
inss=sl*0.08
inssr=round(inss,2)
sind=sl*0.05
sindr=round(sind,2)
slq=sl-(ir+inss+sind)
slqr=round(slq,2)
print('Desconto de IR(11%) R$',irr)
print('Desconto de INSS(8%) R$',inssr)
print('Desconto de SINDICATO(5%) R$',sindr)
print('Seu salário líquido R$', slqr)


