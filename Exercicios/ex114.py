# Crie um código em python que teste se o site pudim está acessível pelo computador usado.
import socket


def internet_on(msg):
    try:
        socket.create_connection((msg, 80))
        return True
    except OSError:
        return False

site = str(input('Informe o site: '))
if internet_on(site):
    print(f'\033[1;33mO site {site} está habilitado.\033[m')
else:
    print(f'\033[1;31mO site {site} está desabilitado.\033[m')
