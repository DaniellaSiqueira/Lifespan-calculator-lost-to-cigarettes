anos = int(input('Fuma há quantos anos?: '))
cigarros = int(input('Quantos ciagarros fuma por dia?: '))
dias_fumando = anos * 365
cigarros_fumados = cigarros * dias_fumando
tempo_perdido = cigarros * dias_fumando
minutos_perdidos = cigarros_fumados * 10
horas_perdidas = minutos_perdidos / 60
dias_perdidos = horas_perdidas / 24
anos_perdidos = dias_perdidos /  365
print (f'Dias fumando: {dias_fumando}')
print (f'Cigarros fumados: {cigarros_fumados}')
print (f'Anos perdidos fumando: {anos_perdidos}')
print (f'Dias perdidos fumando: {dias_perdidos}')
print (f'Horas perdidas fumando: {horas_perdidas}')
print (f'Minutos perdidos fumando: {minutos_perdidos}')


