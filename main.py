import discord
import asyncio

TOKEN = ""
client = discord.Client()
whitelist = {}

async def main():
    print("Script is initializing")
    await asyncio.sleep(15)
    for x in client.guilds:
        if str(x.id) in whitelist:
            print("Keep")
        else:
            try:
                await x.leave()
                print(F"LEFT {x.name}")
            except Exception as brokey:
                print(brokey)
                continue

client.loop.create_task(main())
try:
    client.run(TOKEN, bot=False)
except Exception as e:
    print(e)
