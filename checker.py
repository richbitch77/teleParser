import asyncio
import json
import random
from time import sleep
import bs4 as bs

import requests
from telethon import TelegramClient, functions
from telethon.errors import UsernameNotOccupiedError, UsernameInvalidError, SessionPasswordNeededError, \
    AuthKeyPermEmptyError, FloodWaitError
from english_words import english_words_set
from random_word import RandomWords

SESSIONS_KOLVO = 10


def create_sessions():
    api_id, api_hash = load_configs('src/files/config.json')
    for i in range(SESSIONS_KOLVO):
        print(i)
        with TelegramClient(f'src\\sessions\\session{i}', api_id, api_hash) as client:
            pass


def load_configs(file_path):
    with open(file_path, "r") as f:
        config = json.load(f)
    api_id = config.get('api_id')
    api_hash = config.get('api_hash')
    return api_id, api_hash


def get_name_gen():
    name = RandomWords().get_random_word()
    while len(name) < 5 or len(name) > 9 or name not in english_words_set:
        name = RandomWords().get_random_word()
    return name.lower()


def get_name_file(path):
    names = []
    with open(path, 'r') as f:
        for line in f:
            names.append(line[:-1])
    return names


def write_name(name):
    file1 = open("src\\files\\names.txt", "a")  # append mode
    file1.write(name + '\n')
    file1.close()


def check_on_fragment(name):
    url = 'https://fragment.com/?query=' + name
    try:
        response = requests.get(url)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        first_found = soup.find(class_="table-cell-value tm-value").text[1:]
        availability = ''
        if first_found.__eq__(name):
            availability = soup.find(class_="table-cell-status-thin").text
            if availability.__eq__('Unavailable'):
                return True, 'found'
        return False, availability
    except Exception as e:
        print(e)
        return False, 'exception'


async def parse():
    api_id, api_hash = load_configs('src\\files\\config.json')
    scz = 1
    names = get_name_file('src\\files\\new.txt')
    # while True:
    for name in names:
        async with TelegramClient(f'src\\sessions\\session{scz}', api_id, api_hash) as client:
            try:
                # name = get_name_gen()
                await client(functions.contacts.ResolveUsernameRequest(name))
                print('Taken')
            except UsernameInvalidError as e:
                print('Not available :(')
            except SessionPasswordNeededError as e:
                print('Not available :(')
            except AuthKeyPermEmptyError as e:
                print('Not available :(')
            except UsernameNotOccupiedError as e:
                res, reason = check_on_fragment(name)
                if res:
                    print(f'{name}: Found:)')
                    write_name(name)
                else:
                    print(f'{name}: Not available :( -> {reason}')
            except FloodWaitError as e:
                print(f'Session {scz + 1} has to sleep', e.seconds, 'seconds')

            scz += 1
            scz %= SESSIONS_KOLVO
            sleep(random.randint(3, 10))


if __name__ == '__main__':
    asyncio.run(parse())
    # create_sessions()
