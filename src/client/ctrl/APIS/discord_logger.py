import asyncio
from datetime import datetime

import discord
from discord import Webhook
from discord.file import File
import aiohttp


async def sendNormalMessage_BACKEND(url, title="This is a Test Message from CTRL - MANAGEMENT", description="Just a Plain ol Test message", color_hex="#FFFFFF"):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title=title, description=description, timestamp=datetime.now(), color=discord.Color.from_str(color_hex))
        await webhook.send(embed=embed, username="CTRL - MANAGEMENT - LOG")

async def sendFileMessage_BACKEND(url, title="This is a Test Message from CTRL - MANAGEMENT", description="Just a Plain ol Test message" , file_name="", file_path=None, color_hex="#FFFFFF"):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title=title, description=description, timestamp=datetime.now(), color=discord.Color.from_str(color_hex))
        await webhook.send(embed=embed, username="CTRL - MANAGEMENT - LOGFILE", file=File(filename=file_name, fp=open(file_path, "rb")))



def sendFile(url, title="This is a Test Message from CTRL - MANAGEMENT", description="Just a Plain ol Test message", file_name="log.png", file_path="P:\Phyton\ctrl\src\ctrl\img\icon.png", color_hex="#FFFFFF"):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(sendFileMessage_BACKEND(url, title, description, file_name, file_path, color_hex))
    loop.close()

def logMessage(url, title="This is a Test Message from CTRL - MANAGEMENT", description="Just a Plain ol Test message", color_hex="#FFFFFF"):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(sendNormalMessage_BACKEND(url, title, description, color_hex))
    loop.close()

# sendFile("https://discord.com/api/webhooks/1183838422230650890/zge7RJhXxMHTu3lwB_b4FeEaxDCu65Cheh-EzwbAX6ka1QOR04zSenQYht8yss8Ajm6b")