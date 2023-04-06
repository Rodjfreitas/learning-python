# Crie um código em python que teste se o site pudim está acessível pelo computador usado.
import socket


def internet_on(msg):
    try:
        # Tente conectar-se a um host externo usando um número de porta arbitrário
        # A maioria dos hosts e portas públicas não estão bloqueados
        # Se a conexão for bem-sucedida, a função retornará True
        socket.create_connection((msg, 80))
        return True
    except OSError:
        # Se a conexão falhar, a função retornará False
        return False

site = str(input('Informe o site: '))
if internet_on(site):
    print(f'\033[1;33mO site {site} está habilitado.\033[m')
else:
    print(f'\033[1;31mO site {site} está desabilitado.\033[m')


#Nesse exemplo, a função internet_on tenta criar uma conexão com o host www.google.com na porta 80, que é a porta padrão para o protocolo HTTP. Se a conexão for bem-sucedida, a função retorna True. Se a conexão falhar, a função retorna False.