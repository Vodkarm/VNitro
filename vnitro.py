import random
from colorama import Fore
from time import sleep
from pyfade import Fade, Colors
from pycenter import center

title = """
 __     ___   _ _ _             
 \ \   / / \ | (_) |_ _ __ ___  
  \ \ / /|  \| | | __| '__/ _ \ 
   \ V / | |\  | | |_| | | (_) |
    \_/  |_| \_|_|\__|_|  \___/           https://github.com/Vodkarm/VNitro/edit/main/main.py"""
    
loading = """
______              _____________                        
___  / ____________ ______  /__(_)_____________ _        
__  /  _  __ \  __ `/  __  /__  /__  __ \_  __ `/        
_  /___/ /_/ / /_/ // /_/ / _  / _  / / /  /_/ /________ 
/_____/\____/\__,_/ \__,_/  /_/  /_/ /_/_\__, /_(_)(_)(_)
                                        /____/"""

ready = """
________            _________            ______
___  __ \__________ ______  /____  __    ___  /
__  /_/ /  _ \  __ `/  __  /__  / / /    __  / 
_  _, _//  __/ /_/ // /_/ / _  /_/ /      /_/  
/_/ |_| \___/\__,_/ \__,_/  _\__, /      (_)   
                            /____/"""

print(Fade.Vertical(Colors.red_to_blue, center(title)))
print(f"How many code do you want{Fore.BLUE} generate {Fore.RESET} ?")
print("")
gen = input("")

print(Fade.Vertical(Colors.red_to_blue, center(loading)))
sleep(2)
with open("vnitro-result.txt", "w") as f:
 
  for i in range(int(gen)):
    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    passwd = "http://discord.gift/"
    for i in range(16): passwd = passwd + element[random.randint(0, len(element) - 1)]
    print(f"[{Fore.GREEN}GEN{Fore.RESET}] {Fore.BLUE}{passwd}{Fore.RESET}")

    f.write(f"{passwd}\n")
    
print(Fade.Vertical(Colors.red_to_green, center(ready)))
print("Your nitro codes is " + Fore.GREEN + "ready " + Fore.RESET + "in vnitro-result.txt")
