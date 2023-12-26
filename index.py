##from socket import gethostname, gethostbyname
## https://ipinfo.io/json
## http://ip-api.com/json/IP_HERE?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,mobile,proxy,hosting,query
import time
import requests
import os
import colorama
import pyfiglet
from googletrans import Translator

translator = Translator()

opt = ['Realizar busca por IP']

def get_colorBy(colorname='RED'):
    return colorama.Fore.RED

def startloop():
    print('Começando a Busca, aguarde...')
    time.sleep(1.5)
    for i in range(13560):
        print('Coletando informações (Esta mensagem pode aparecer inúmeras vezes)')
        print('Aprimorando Busca (Esta mensagem pode aparecer inúmeras vezes)')
        print('Transformando em algo de possível leitura (Esta mensagem pode aparecer inúmeras vezes)')
    os.system('cls')
    print(colorama.Fore.GREEN + 'Feito!')
    time.sleep(2.33)
    os.system('cls')
    time.sleep(3)
    
def search_ip():
    api = 'http://ip-api.com/json/IP_HERE?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,mobile,proxy,hosting,query'
    res = input('Informe o IP:\n>> ')
    api = api.replace('IP_HERE', f'{res}')
    info = requests.get(api)
    response = info.json()
    os.system('cls')
    if info.status_code != 403:
        startloop()
        print(f'''
\tContinente: {response['continent']} ({response['continentCode']})\n
País atual do IP: {response['country']} ({response['countryCode']})\n
Estado: {response['regionName']} ({response['region']})\n
Cidade: {response['city']}\n
Distrito: {response['district']}
CEP: {response['zip']}
\n\t## INFORMAÇÕES GERAIS ##\n
Fuso Horário: {response['timezone']}\n
Moeda do país: {response['currency']}\n
Empresa que está fornecendo Internet: {response['org']}\n
Está no celular?: {response['mobile']}\n
Está usando proxy/VPN?: {response['proxy']}\n
Internet hotspot? (Está hosteando para outras pessoas): {response['hosting']}\n
\t##INFORMAÇÕES GEOGRAFICAS##\n
Latitude: {response['lat']}\n
Longitude: {response['lon']}
                ''')
        with open(res+'.txt', 'w') as file:
            file.write(f'''
\tContinente: {response['continent']} ({response['continentCode']})\n
País atual do IP: {response['country']} ({response['countryCode']})\n
Estado: {response['regionName']} ({response['region']})\n
Cidade: {response['city']}\n
Distrito: {response['district']}
CEP: {response['zip']}
\n\t## INFORMAÇÕES GERAIS ##\n
Fuso Horário: {response['timezone']}\n
Moeda do país: {response['currency']}\n
Empresa que está fornecendo Internet: {response['org']}\n
Está no celular?: {response['mobile']}\n
Está usando proxy/VPN?: {response['proxy']}\n
Internet hotspot? (Está hosteando para outras pessoas): {response['hosting']}\n
\t##INFORMAÇÕES GEOGRAFICAS##\n
Latitude: {response['lat']}\n
Longitude: {response['lon']}
''')

def shrug():
    return "¯\_(ツ)_/¯"

print(get_colorBy(),
      f'''
      {pyfiglet.figlet_format('Ballora')}\n made by Gustavo \n\n(Isso foi criado pois não tinha o que fazer {shrug()} )
''')
for i, e in enumerate(opt, 1):
    print(f'{colorama.Fore.BLUE + "["}{colorama.Fore.YELLOW+str(i)}{colorama.Fore.BLUE + "] "}{colorama.Fore.RED + e}')

res = input(colorama.Fore.RESET + ">> ")

if res.isnumeric() and int(res) in range(1, len(opt) + 1):
    if int(res) == 1:
        search_ip()
else: 
    print('Digite apenas números/números correspondentes nas opções. Reabra o exec')
    time.sleep(3)
    os.system('cls')
