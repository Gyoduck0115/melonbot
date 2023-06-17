import chart
import discord

with open('./token.txt') as f:
    TOKEN = f.read()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # "$멜론차트" 라고만 쓰면 1등~10등까지 보여준다
    if message.content == '멜론차트':
        await message.channel.send(chart.get_top_ten_string())

    # "$멜론차트 x" 라고 쓰면 x등을 보여준다. 근데 x는 1~10
    elif message.content.startswith('멜론차트'):
        top_ten_singer, top_ten_song = chart.get_top_ten()

        x = int(message.content[5:])
        # x 값이 1~10일 때만 아래 실행
        if 0 < x < 11:
            song1 = top_ten_song[x-1]
            await message.channel.send(f"{x}등 : "+song1)
        
        


client.run(TOKEN)



