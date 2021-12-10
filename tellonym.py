import requests
import random
from colorama import *
g = Fore.GREEN
r = Fore.RED
y = Fore.YELLOW
c = Fore.CYAN
print(r + '''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁ ''')
print(c+'================================================')
print('==========INSTAGRAM@dqfa======SNAPCHAT:UBHC=====')
print('====================GITHUB:0xDARTH==============')


rt = requests.session()
litters = 'qwertyuiopasdfghjklzxcvbnm1234567890._'
u = ''

us = input("[1] User length from 4\n[2] User length from 3\n====>")

id = input("[+] Enter Id : ")

token = input("[+] Enter Bot Token : ")
print('')
print('================================================')

hea = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
'cookie': '_ga=GA1.2.39934708.1635545492; _gid=GA1.2.537994784.1635545492; _gat=1; __cf_bm=xta9Nel914ITv93ISUDXGG_gU57Jju5VrEETAvVPrEo-1635549346-0-ARufJukWRqiF49dFjFbHF1lHOF4gept1uUdtUBdg4Pjr1hdt387WzBcsUhcHHE64oamXK0AaR4d6W/gjK42YVRheE232A00APpRkfEq5aNvROJWRXm1jEw+4/l3oABx9ZQ==; __rtgt_sid=kvczup60lfgb3q',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    }
if us == "1":
    while True:
        user = str("".join(random.choice(litters)for x in range(0)))
        user1 = str("".join(random.choice(litters)for x in range(4)))
        usernames = user + u + user1
        tiko = f'https://tellonym.me/{usernames}'
        reqsnd = rt.get(tiko, headers=hea).status_code
        if reqsnd == 404:
         print(g + f' [+] available : {usernames} ')
         bot = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= available : {usernames}\n𝘽𝙔 : @dqfa"
         rt.get(bot)
        else:
          print(r + f' [+] Unavailable : {usernames}  ')
if us == "2":
    while True:
        user = str("".join(random.choice(litters)for x in range(0)))
        user1 = str("".join(random.choice(litters)for x in range(3)))
        usernames = user + u + user1
        tiko = f'https://tellonym.me/{usernames}'
        reqsnd = rt.get(tiko, headers=hea).status_code
        if reqsnd == 404:
         print(g + f' [+] available : {usernames} ')
         bot = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text= available : {usernames}\n𝘽𝙔 : @dqfa"
         rt.get(bot)
        else:
          print(r + f' [+] Unavailable : {usernames}  ')
