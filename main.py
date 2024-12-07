import asyncio
from random import choice, random, shuffle
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
        balance INTEGER DEFAULT 50,
        high_score INTEGER DEFAULT 0,
        user_name TEXT 
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
    cursor.execute("SELECT user_name, high_score, balance FROM gulungus_economy ORDER BY high_score DESC LIMIT 10")
    leaderBoard = cursor.fetchall()
    embed = discord.Embed(title="Leaderboard", description="Here are the top users", color=0x00ff00)  # You can customize the title, description, and color
    if leaderBoard:
        for user_name, high_score, balance in leaderBoard:
            embed.add_field(name=user_name, value=f"Score: {high_score}", inline=False)
            # "Score: {high_score}\nBalance: ${balance}" if i want to add the balance
    else:
         embed.description = "No entires found"
    embed.set_footer(text="This is the leaderboard footer")
    await message.channel.send(embed=embed)
    
async def handle_balance(message: Message):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower() in ['leaderboard']
    user_id = str(message.author.id)
    user_name_curr = str(message.author.display_name)
    cursor.execute("SELECT balance, user_name FROM gulungus_economy WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    balance = result[0]
    user_name = result[1]
    if user_name_curr != user_name:
        cursor.execute("UPDATE gulungus_economy SET user_name = ? WHERE user_id = ?", (user_name_curr, user_id))
        user_name = user_name_curr
    embed = discord.Embed(title="Balance", description="", color=0x00ff00)
    if result:
        print("test")
        embed.add_field(name=user_name, value=f"Balance: ${balance}", inline=False)
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
    user_id = str(message.author.id)
    username = str(message.author.display_name)
    
   #if user_id not in throwbreakstreak:
    #    throwbreakstreak[user_id] = 0
    #SQL WORK IN PROGRESS####################
    
    
    conn = sqlite3.connect('gulungus_economy.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO gulungus_economy (user_id, balance, high_score, user_name) VALUES (?, ?, ?, ?)", (user_id, 0, 0, username))
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
    user_id = str(message.author.id)
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM gulungus_economy WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    userBalance = result[0]
    sessionScore = 0
    message_pieces = message.content.split()
    userWager = int(message_pieces[1])
    user_name= str(message.author.display_name)
    print(message_pieces[1])
    if len(message_pieces) < 2 or not message_pieces[1].isdigit():
        await message.channel.send("Invalid input. Use the format !50/50 <amount>")
        return
    
    
    if userBalance < int(message_pieces[1]):
        await message.channel.send("Not enough cash stranger")
        return
  
    
        
        
    while True:
        await message.channel.send('Choose low or mid (or type "exit" to quit):')
        try:
        
            user_guess = await client.wait_for('message', check=check, timeout=30.0)  
            coin_flip = choice(['low', 'mid'])
            if user_guess.content.lower() == coin_flip:
                await message.channel.send("YOU WIN")
                cursor.execute("UPDATE gulungus_economy SET balance = ? WHERE user_id = ?", ((userBalance + userWager), user_id))
                newBalance = userBalance + userWager
              
            else:
                await message.channel.send("YOU LOSE")
                cursor.execute("UPDATE gulungus_economy SET balance = ? WHERE user_id = ?", ((userBalance - userWager), user_id))
                newBalance = userBalance - userWager
                
                
                                
            embed = discord.Embed(title="New Balance", description="", color=0x00ff00)
            embed.add_field(name=user_name, value=f"Balance: ${newBalance}", inline=False)
            await message.channel.send(embed=embed)
            conn.commit()
            break
        except asyncio.TimeoutError:  
            await message.channel.send('You took too long to respond.')
            break  
        
      

async def handle_blackjack(client, message: Message, user_message: str):
    def check(m):
        return m.author == message.author and m.channel == message.channel and m.content.lower() in ['low', 'mid']
  
    user_id = str(message.author.id)
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM gulungus_economy WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    userBalance = result[0]
    sessionScore = 0
    messagePieces = message.content.split()
    userWager = int(messagePieces[1])
    userName= str(message.author.display_name)
    print(messagePieces[1])
    if len(messagePieces) < 2 or not messagePieces[1].isdigit():
        await message.channel.send("Invalid input. Use the format !50/50 <amount>")
        return
    if userBalance < int(messagePieces[1]):
        await message.channel.send("Not enough cash stranger")
        return
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = [
    {"rank": "Ace", "value": 11, "emoji": "🂡"},  
    {"rank": "2", "value": 2, "emoji": "🂢"},
    {"rank": "3", "value": 3, "emoji": "🂣"},
    {"rank": "4", "value": 4, "emoji": "🂤"},
    {"rank": "5", "value": 5, "emoji": "🂥"},
    {"rank": "6", "value": 6, "emoji": "🂦"},
    {"rank": "7", "value": 7, "emoji": "🂧"},
    {"rank": "8", "value": 8, "emoji": "🂨"},
    {"rank": "9", "value": 9, "emoji": "🂩"},
    {"rank": "10", "value": 10, "emoji": "🂪"},
    {"rank": "Jack", "value": 10, "emoji": "🂫"},
    {"rank": "Queen", "value": 10, "emoji": "🂭"},
    {"rank": "King", "value": 10, "emoji": "🂮"},
    ]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append({
            "suit": suit,
            "rank": rank["rank"],
            "value": rank["value"],
            "emoji": rank["emoji"]
        })
    for card in deck:
        print(f"{card['emoji']} {card['rank']} of {card['suit']} (Value: {card['value']})")
    shuffle(deck)
    drawnCard = deck.pop()
    print(drawnCard)
    drawnCard2 = deck.pop()
    print(drawnCard2)
    playerHand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop(), deck.pop()]
    playerTotal = sum(card["value"] for card in playerHand)
    dealerTotal = sum(card["value"] for card in dealerHand)
    
    gameMessage = await blackjackEmbed(message, playerHand, playerTotal, dealerHand, dealerTotal, outcome=None, gameMessage =None)
    while True:
        if playerTotal == 21:
            gameMessage = await blackjackEmbed(message, playerHand, playerTotal, dealerHand, dealerTotal, "win", gameMessage)
            break
        if playerTotal > 21:
            gameMessage = await blackjackEmbed(message, playerHand, playerTotal, dealerHand, dealerTotal, "lose", gameMessage)
            break    
        await message.channel.send("React with 🆙 to Hit or 🛑 to Stand.")
        await gameMessage.add_reaction("🆙")
        await gameMessage.add_reaction("🛑")
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ["🆙", "🛑"]

        reaction, user = await client.wait_for("reaction_add", check=check)
        if playerTotal > 21:
            await message.channel.send("you bussssted")
              
            break
        elif str(reaction.emoji) == "🛑":
            while dealerTotal < 17:
                dealerHand.append(deck.pop())
                dealerTotal = sum(card["value"] for card in dealerHand)
               # await blackjackEmbed(message, playerHand, playerTotal, dealerTotal) # might not need thisx
            if dealerTotal > 21:
                await gameMessage.edit(content="DEALER BUSTED!")
                outcome = "win"
            elif dealerTotal > playerTotal:
                await gameMessage.edit(content="Dealer wins.")
                outcome = "lose"
            elif dealerTotal == playerTotal:
                await gameMessage.edit(content="Tie, nobody wins.")
                outcome = "tie"
            elif playerTotal > dealerTotal:
                await gameMessage.edit(content="You win!")
                outcome = "win"
            gameMessage = await blackjackEmbed(message, playerHand, playerTotal, dealerHand, dealerTotal, outcome, gameMessage)
            print("the last shit probably")
            break
            
        elif str(reaction.emoji) == "🆙":
            playerHand.append(deck.pop())
            playerTotal = sum(card["value"] for card in playerHand)
            if playerTotal > 21:
                gameMessage = await blackjackEmbed(message, playerHand, playerTotal, dealerHand, dealerTotal, "lose", gameMessage)
                break
            else:
                await gameMessage.clear_reactions()
                await gameMessage.add_reaction("🆙")  
                await gameMessage.add_reaction("🛑")  
                gameMessage = await blackjackEmbed(message, playerHand, playerTotal, dealerHand, dealerTotal, None, gameMessage)
                
                
            

            
    

    print(f"Drawn Card: {drawnCard['emoji']} {drawnCard['rank']} of {drawnCard['suit']}")
    print(f"Remaining Cards: {len(deck)}")  

    
   
    
    
async def blackjackEmbed(message, playerHand, playerTotal, dealerHand, dealerTotal, outcome=None, gameMessage=None):
    player_hand_display = " ".join([card["emoji"] for card in playerHand])
    if outcome:
        dealer_hand_display = " ".join([card["emoji"] for card in dealerHand])  # Reveal full dealer hand
    else:
        dealer_hand_display = " ".join([card["emoji"] for card in dealerHand[:-1]]) + " ❓"  # Hide second card
    print("do i get here")
    print(outcome)
    embed = discord.Embed(
        title="Blackjack Game",
        description=f"**Your Hand:** {player_hand_display}\n**Dealer's Hand:** {dealer_hand_display}",
        color=discord.Color.blue()
    )
    if outcome:
        if outcome == "win":
            embed.color = discord.Color.green()  
            embed.description += "\n**You win!**"
        elif outcome == "lose":
            embed.color = discord.Color.red()  
            embed.description += "\n**Dealer wins.**"
        elif outcome == "tie":
            embed.color = discord.Color.gold()  
            embed.description += "\n**It's a tie!**"
    
    
    embed.add_field(name="Your Total", value=str(playerTotal), inline=False)
    embed.add_field(name="Dealer's Total", value=f"{dealerTotal} (hidden)", inline=False)
    if gameMessage:
        await gameMessage.edit(embed=embed)
        print("do i get here POOPY")
    else:  
        gameMessage = await message.channel.send(embed=embed)
    return gameMessage
    
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
            if 'bj' in user_message:
                await handle_blackjack(client, message, user_message)
            
            
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