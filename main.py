import asyncio
from random import choice
from typing import Final
import os 
import sqlite3

from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from discord import Embed  
import discord


#LOAD TOKEN
load_dotenv()
print("hi")
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

#BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
#
# OLD MAP STUFF
user_scores = {}

#NEW SQL STUFF
conn = sqlite3.connect('gulungus_economy.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS gulungus_economy (
        user_id TEXT PRIMARY KEY,
        balance INTEGER DEFAULT 0,
        high_score INTEGER DEFAULT 0
    )
''')
conn.commit()


#MESSAGE

async def handle_leaderBoard(message: Message):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower() in ['leaderboard']
    sorted_throwbreakstreak = dict(sorted(throwbreakstreak.items(), key=lambda item: item[1], reverse=True))
    print(sorted_throwbreakstreak)
    embed = discord.Embed(title="Leaderboard", description="Here are the top users", color=0x00ff00)  # You can customize the title, description, and color
    for name, score in sorted_throwbreakstreak.items():
        embed.add_field(name=name, value=f"Score: {score}", inline=False)
    else:
        embed.set_footer(text="This is the leaderboard footer")

    await message.channel.send(embed=embed)
    
async def handle_leaderBoard_SQL(message: Message):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower() in ['leaderboard']
    cursor.execute("SELECT user_id, high_score, balance FROM gulungus_economy ORDER BY high_score DESC LIMIT 10")
    leaderBoard = cursor.fetchall()
    embed = discord.Embed(title="Leaderboard", description="Here are the top users", color=0x00ff00)  # You can customize the title, description, and color
    if leaderBoard:
        for user_id, high_score, balance in leaderBoard:
            embed.add_field(name=user_id, value=f"Score: {high_score}", inline=False)
            # "Score: {high_score}\nBalance: ${balance}" if i want to add the balance
    else:
         embed.description = "No entires found"
    embed.set_footer(text="This is the leaderboard footer")
    await message.channel.send(embed=embed)
    
async def handle_balance(message: Message):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower() in ['leaderboard']
    user_id = str(message.author.display_name)
    cursor.execute("SELECT balance FROM gulungus_economy WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    balance = result[0]
    embed = discord.Embed(title="Balance", description="", color=0x00ff00)
    if result:
        print("test")
        embed.add_field(name=user_id, value=f"Balance: ${balance}", inline=False)
    await message.channel.send(embed=embed)
    
    
    
    
    
    # if result:
    #     for user_id, high_score, balance in result:
    #         embed.add_field(name=user_id, value=f"Balance: {balance}", inline=False)
    #         # "Score: {high_score}\nBalance: ${balance}" if i want to add the balance
    # await message.channel.send(embed=embed)
            
            
    
    
    

        
async def update_highscore(message: Message, user_id, sessionScore):
    cursor = conn.cursor()
    cursor.execute("SELECT high_score FROM gulungus_economy WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    if result:
        current_highscore = result[0]
    if sessionScore > current_highscore:
        cursor.execute("UPDATE gulungus_economy SET high_score = ? WHERE user_id = ?", (sessionScore, user_id))
        conn.commit()  
        await message.channel.send(f'New highscore of {sessionScore}!')
    await message.channel.send(f'Score of  {sessionScore}!')
    
    
async def update_balance(message: Message, user_id, sessionScore):
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM gulungus_economy WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    if result:
        current_balance = result[0]
    cursor.execute("UPDATE gulungus_economy SET balance = ? WHERE user_id = ?", ((current_balance+sessionScore), user_id))
    conn.commit()
    await message.channel.send(f'balance of  {current_balance + sessionScore}!')
    
    

    
    
    
    
    
async def handle_throw_test(message: Message):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower() in ['throwtest', '1', '2', '12']
    user_id = str(message.author.display_name)
    
   #if user_id not in throwbreakstreak:
    #    throwbreakstreak[user_id] = 0
    #SQL WORK IN PROGRESS####################
    
    
    conn = sqlite3.connect('gulungus_economy.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO gulungus_economy (user_id, balance, high_score) VALUES (?, ?, ?)", (user_id, 0, 0))
    conn.commit()
    
    

        
        
        
    sessionScore = 0
    await message.channel.send('``u have now entered throw test``')
    while True:
        try:
            coin_flip = choice(['1', '2', '12'])
            coin_flip_character = choice([1, 2 , 3])
            #Chara 1 = paul, chara 2 = drag chara 3 = king
            print(coin_flip)
            if coin_flip == '12':
                if coin_flip_character == 1:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/732775000372805634/1286981380277800992/gromp.gif?ex=66efe250&is=66ee90d0&hm=dbff5181a9c43f9362b228d60aff8440ce457803d1716fe6e649b86c43df690b&'
                if coin_flip_character == 2:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/1088293164957315202/1298175422013374516/grompington.gif?ex=67189b93&is=67174a13&hm=a867834dadba518f2dd59f99c41d1b442a5ee70282c9827ac569ee542e9d7bad&'   
                if coin_flip_character == 3:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/755870190411055249/1298186638106693672/gromp1ngton.gif?ex=6718a605&is=67175485&hm=95022f12db9d9b136b37500ab77c8c09b4dcbf652a134b6261844eaadf9c7596&'
            if coin_flip == '1':
                if coin_flip_character == 1:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/732775000372805634/1286981323579330663/paulthrow.gif?ex=66efe242&is=66ee90c2&hm=a9fe1af456219931c43ac6c3ed43f5418f8e93369f649caddc19583751a626c1&'
                if coin_flip_character == 2:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/1088293164957315202/1298175421631696916/grompuloid.gif?ex=67189b93&is=67174a13&hm=7d73ac9638672dd2516184561c805b21afc6bd50ca06feac85e36a12742d58cf&'
                if coin_flip_character == 3:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/755870190411055249/1298186851747627099/gr0mpington.gif?ex=6718a638&is=671754b8&hm=2eecc3bc051eef6155243e9332685f0291296eaeafcd4fdfc2eaa93d204d35bf&'
            if coin_flip == '2':
                if coin_flip_character == 1:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/732775000372805634/1286981358392184932/paulthrowington.gif?ex=66efe24a&is=66ee90ca&hm=c463ccc3deedc8dae761761d6b1af9597ab1d251d3d138bd31d47a52046f5cd8&'
                if coin_flip_character == 2:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/1088293164957315202/1298175422357569639/grompula.gif?ex=67189b93&is=67174a13&hm=626150c395fb4498ff51ff1e3a0ca6e5cc38cfe60b57a29e853d6fd5baf73c89&'
                if coin_flip_character == 3:
                    throwtoBreak = 'https://cdn.discordapp.com/attachments/755870190411055249/1298187172817403956/king2break.gif?ex=6718a685&is=67175505&hm=d9e39936ccaa88a4d5cc81bcda7b7dc470210ca77a46bf615c7121724c87f50c&'
            await message.channel.send(throwtoBreak)
            user_guess = await client.wait_for('message', check=check, timeout=3.0) 
            print(user_guess)
            print(f"User guessed: {user_guess.content}, Expected: {coin_flip}")
            if user_guess.content.lower() == coin_flip:
                sessionScore += 1
                await message.channel.send(f'Current streak is {sessionScore}')
            if user_guess.content.lower() != coin_flip:
                await message.channel.send(f'That was a {coin_flip} break')
                await update_highscore(message, user_id, sessionScore)
                await update_balance(message, user_id, sessionScore)
              #  if throwbreakstreak[user_id] < sessionScore:
                     #   await message.channel.send(f'new highscore of {sessionScore}')
               #         throwbreakstreak[user_id] = sessionScore
                      
                      #  await message.channel.send(throwbreakstreak[user_id])
                break
        except asyncio.TimeoutError:
            await message.channel.send('You took too long')
            await update_highscore(message, user_id, sessionScore)
            await update_balance(message, user_id, sessionScore)
            #if throwbreakstreak[user_id] < sessionScore:
                 #   await message.channel.send(f'new highscore of {sessionScore}')
             #       throwbreakstreak[user_id] = sessionScore
                 #   await message.channel.send(throwbreakstreak[user_id])
                 
                
            break       
    
async def handle_5050_response_tekken(message: Message, user_message: str):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower() in ['low', 'mid']
    
    user_id = str(message.author.display_name)
    if user_id not in user_scores:
        user_scores[user_id] = 0
    sessionScore = 0
    
        
        
    while True:
        await message.channel.send('Choose low or mid (or type "exit" to quit):')
        try:
        
            user_guess = await client.wait_for('message', check=check, timeout=30.0)  
            coin_flip = choice(['low', 'mid'])
            if user_guess.content.lower() == coin_flip:
                sessionScore += 1
                await message.channel.send(f'ur goated, current streak is {sessionScore}' )
            else:
                await message.channel.send("ur trash")
                if user_scores[user_id] < sessionScore:
                    await message.channel.send(f'new highscore of {sessionScore}')
                    user_scores[user_id] = sessionScore
                await message.channel.send(user_scores[user_id])
                break
        except asyncio.TimeoutError:
            await message.channel.send('You took too long')
            break

        
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because intents were not enabled")
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    elif is_public := user_message[0] == '!':
        user_message = user_message[1:]

        
    try:
        
        response: str = get_response(user_message)
        if is_private:
            await message.author.send(response)
        elif is_public:
            await message.channel.send(response)
            if '50/50' in user_message:
                await handle_5050_response_tekken(message, user_message)
            if 'throwtest' in user_message:
                await handle_throw_test(message)
            if 'leaderboard' in user_message:
                await handle_leaderBoard_SQL(message)
            if 'balance' in user_message:
                await handle_balance(message)
            
            
    except Exception as e:
        print(e)
        
#STEP 3
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username} "{user_message}"')
    await send_message (message, user_message)
    
#ENTRY POINT
def main() -> None:
    print("hi")
    client.run(token= TOKEN)
if __name__ == '__main__':
    print("test")
    main()