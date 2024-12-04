from random import choice, randint




def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    poopy = 'https://cdn.discordapp.com/attachments/1021301690202325052/1286968923735986227/12break.gif?ex=66efd6b6&is=66ee8536&hm=311a05d6bf10c96d5e43279fc236c40175c007a45765ff7915e7ba5fa6e28840&'

    if lowered == '':
        return 'amonga'
    elif 'hello' in lowered:
        return 'big dawg'
    elif 'roll shit' in lowered:
        return f'you rolled: {randint(1,6)}'
    elif 'mrbeast' in lowered:
        return poopy 
    elif '50/50' in lowered:
        return 'type low or mid to gamble'
        
    else:
        return choice(['this shit aint nothing to me man', 'gulungus', 'idk'])
    