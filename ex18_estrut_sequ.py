# Q18_17Estrutura sequencial _https://wiki.python.org.br/EstruturaSequencial
# Downlod
arq=int(input('Informe o tamanho do seu arquivo (MB): '))
li_v=float(input('Informe a velocidade da conexão(Mbps): '))
tm_down=arq/li_v
tm_sr=round(tm_down,1)
td_min=tm_sr*60
tm_mr=round(td_min,1)
t_tm=arq/tm_mr
t_tmr=round(t_tm,1)

print('Velocidadede download/seg=',tm_sr,'Mbps.')
print('Velocidadede download/min=',td_min,'Mbpm.')
print('Tempo aproximado de duração download=',t_tmr,'minutos.')




