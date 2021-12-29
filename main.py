import os
import random
import discord
import json
import requests
from requests import Request, Session

from discord.ext import commands
from dotenv import load_dotenv


# data z bitcoinu / ziskavanie dat BTC  // getting data from URLjson type this one specially printing ID and current_price into console

def getCryptoPrices(crypto):                # function to get data from URL
    URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    r = requests.get(url=URL)
    data = r.json()
    print(data[0]['id'])
    print(data[0]['current_price'])




getCryptoPrices('bitcoin')      # calling a function // vyzva k vykonaniu funkcie 


load_dotenv()


prefix = '.'          # prefix (we wont use that since i changed my mind but its here just for sure i wanted to add prefix) // deklaracie prefixu

TOKEN = "###"           # token from discord developer portal, for security reasons its deleted here, insert your token


client = discord.Client()               # declaration of the client 

#client event na zapnutie bota (on_ready) sa vykona vypis do konzole ze bot sa napojil, sluzi ako kontrola spravneho pripojenia
# (ENG) client event to turn on bot, when it will turn on it will display print(), that is for make sure that our bot is working
@client.event
async def on_ready():
    print(f'{client.user.name} sa uspesne napojil na discord')


@client.event
async def on_message(message):                          #message function on message
    if message.author == client.user:
        return

    if message.content == 'hello' :                     # if statement
        await message.channel.send("hi")                # bot will respond


    if message.content == 'cena' or message.content == 'price'  :   # if my message is cena or price it will start IF statement
        URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'  # URL (api) from where we are getting these data
        r = requests.get(url=URL)   # declaration of "r" as requests (from import requests).get url which is declared above me
        data = r.json()         # declaration of "data" which is "r" (requestes data from json URL) . json()
        print(data[0]['id'])    #printing data[0] "ID" into console, NOT INTO DISCORD!
        print(data[0]['current_price'])        #same with "current_price"
        print(data[0]['price_change_percentage_24h'])   #same with price change with percentage
        await message.channel.send(data[0]['current_price'])  #finally bot respond with current_priced, you can also include ID as well but i did not
        await message.channel.send('percentuálna zmena ceny za 24hodín:')
        await message.channel.send(data[0]['price_change_percentage_24h'])

    
                    


client.run(TOKEN)
