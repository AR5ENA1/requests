import requests

characters = ['hulk', 'captain america', 'thanos']


def characteristic(name):
    """Получение характеристики героя"""
    character = (requests.get(f'https://www.superheroapi.com/api/2619421814940190/search/{name}').json())
    character_intelligence = character['results'][0]['powerstats']['intelligence']
    return character_intelligence


def max_int(characters):
    """Получение героя с max intelligence"""
    best_character = None
    num = 0

    for character in characters:
        intelligence = int(characteristic(character))
        if intelligence > num:
            best_character = character
    return best_character


print(f'Герой с самым высоким intelligence: {max_int(characters)}')