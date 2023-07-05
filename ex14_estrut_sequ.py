# Q14_Estrutura sequencial _https://wiki.python.org.br/EstruturaSequencial
# João pescador

print('OLÁ JOÃO!')
pt=float(input('Informe o peso total(Kg) pescado hoje: '))
pe=float(pt-50)
per=round(pe,2)
ml=float(pe*4.00)
mlr=round(ml,2)
if pt<=50:
    print('Hoje não tem multa João. Bom descanso!')
else:
     print('João o excesso de hj em Kg foi ',per)
     print('A multa gerada é de R$',mlr)
