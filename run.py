import discord
import asyncio
import random

from discord.utils import get


client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('집가고싶다') 
    await client.change_presence(status=discord.Status.online, activity=game)
    
    
    
@client.event
async def on_message(message):
    if message.content == ("시진"): 
        await message.channel.send (f"핑핑이") 


        

client.run("MTAwOTAyNTIzNjUxMzA4MzQyMw.GvkKks.ysl0AD7Nd8ve936bdrFzjQLyyqZHjN42MDZGek") 