from random import choice, randint




def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    poopy = 'https://tenor.com/view/mrbeast-squid-game-mr-beast-gif-24004413'

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
    