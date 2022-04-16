import random
from colorama import Fore
from time import sleep
from pystyle import Colorate, Colors
from pycenter import center

title = """
 __     ___   _ _ _             
 \ \   / / \ | (_) |_ _ __ ___  
  \ \ / /|  \| | | __| '__/ _ \ 
   \ V / | |\  | | |_| | | (_) |
    \_/  |_| \_|_|\__|_|  \___/           https://github.com/Vodkarm/VNitro/"""

print(Colorate.Vertical(Colors.red_to_blue, center(title), 1))
print(f"How many codes do you want{Fore.BLUE} generate {Fore.RESET} ?")
print("")
gen = input("")

with open("vnitro-result.txt", "w") as f:
 
  for i in range(int(gen)):
    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    passwd = "http://discord.gift/"
    for i in range(16): passwd = passwd + element[random.randint(0, len(element) - 1)]
    print(f"[{Fore.GREEN}GEN{Fore.RESET}] {Fore.BLUE}{passwd}{Fore.RESET}")

    f.write(f"{passwd}\n")
    
print("Your nitro codes was " + Fore.GREEN + "generated " + Fore.RESET + "in vnitro-result.txt")
