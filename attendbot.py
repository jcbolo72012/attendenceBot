import discord
import asyncio

client = discord.Client()
id = input("Input Channel ID:")
@client.event
async def on_ready():
    vc = client.get_channel(id) #get the id of the voice channel
    attend = vc.members
    f = open('Attendees.txt', 'w+')
    f.write('\n'.join([user.name for user in attend]))
    f.close()

variable = input("P")
asyncio.run(on_ready())
variable = input("P")
