import os

def inicio():
    try:
        print('''
Packlist v1.0        
        ''')
        ano = input('Ano: ')
        mes = input('Mês: ')
        dia = input('Dia: ')
        os.system('clear')
        print('''
Packlist v1.0

Pacotes instalados em {}/{}/{}
        '''.format(dia, mes, ano))
        grep = ('grep "{}-{}-{}.*.install " /var/log/dpkg.log '.format(ano, mes, dia))
        awk = ('| awk \'{ print $4 }\' ')
        cut = ('| cut -d: -f1')
        os.system(grep + awk + cut)
        print('')

    except KeyboardInterrupt:
        print('\nInterrompido...')

if __name__ == "__main__":
    inicio()