import requests
import pygame
from time import sleep
import datetime
import json


def oneline(flush):
    try:
        print('')
    except Exception as e:
        print(f'error:{e}')


oneline(flush=True)

SCREEN_W = 1200
SCREEN_H = 400

pygame.init()

img = pygame.image.load('print.png')
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
sleep(2)
screen.blit(img, (0, 0))
pygame.display.update()

r1 = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacao = json.loads(r1.text)

sleep(3)
oneline(flush=True)
print(f'//{cotacao}//', flush=True)
oneline(flush=True)
sleep(3)

sair = False
while not sair:
    sleep(1)
    oneline(flush=True)
    opc = str(input('Digite a moeda:'))
    if opc == 'SAIR':
        sair = True

    if opc == 'dollar':
        sleep(1)
        print(cotacao['USD']['name'], flush=True)
        print('valor:', cotacao['USD']['high'], flush=True)

    if opc == 'dollar_cad':
        sleep(1)
        print(cotacao['CAD']['name'], flush=True)
        print(cotacao['CAD']['high'], flush=True)

    if opc == 'euro':
        sleep(1)
        print(cotacao['EUR']['name'], flush=True)
        print('valor:', cotacao['EUR']['high'], flush=True)

    if opc == 'iene':
        sleep(1)
        print(cotacao['JPY']['name'], flush=True)
        print('valor:', cotacao['JPY']['high'], flush=True)

    if opc == 'bitcoin':
        sleep(1)
        print(cotacao['BTC']['name'], flush=True)
        print('valor:', cotacao['BTC']['high'], flush=True)

    if opc == 'ethereum':
        sleep(1)
        print(cotacao['ETH']['name'], flush=True)
        print('valor:', cotacao['ETH']['high'], flush=True)

    if opc == 'dogecoin':
        sleep(1)
        print(cotacao['DOGE']['name'], flush=True)
        print('valor:', cotacao['DOGE']['high'], flush=True)

    if opc == 'xrp':
        print(cotacao['XRP']['name'])
        print('valor:', cotacao['XRP']['high'])

    if opc == 'libra':
        print(cotacao['GBP']['name'])
        print('valor:', cotacao['GBP']['high'])

time = datetime.datetime.now()
print(f'ultimo acesso>> {time}')