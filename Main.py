import random
import string
import time
from colorama import Fore, init

init(autoreset=True)

def generate_nitro_code():
    
    return "https://discord.gift/" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def is_valid_code(code):

    return code[17] in "123456789"


def print_ascii_art():
    ascii_art = """
██████╗ ██╗     ██╗   ██╗███████╗██████╗ ███████╗██████╗ 
██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
██████╔╝██║     ██║   ██║█████╗  ██████╔╝█████╗  ██║  ██║
██╔══██╗██║     ██║   ██║██╔══╝  ██╔══██╗██╔══╝  ██║  ██║
██████╔╝███████╗╚██████╔╝███████╗██║  ██║███████╗██████╔╝
╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                         
                                                         @developed by: Alex | betanoro on discord
                                                         Version: 1.0
    """

    print(Fore.MAGENTA + ascii_art)

def main():

    print_ascii_art()
    print(Fore.GREEN + "Ayoo welcome at discord nitro Generator!")
    print(Fore.CYAN + "How much codes?")


    try:
        num_codes = int(input(Fore.YELLOW + "Număr coduri: "))
    except ValueError:
        print(Fore.RED + "Te rog să introduci un număr valid!")
        return

    if num_codes <= 0:
        print(Fore.RED + "Numărul de coduri trebuie să fie mai mare decât 0.")
        return

    print(Fore.GREEN + f"Generând {num_codes} coduri Discord Nitro...\n")

    for i in range(num_codes):
        code = generate_nitro_code()

        if is_valid_code(code):
            status = "[VALID]"
        else:
            status = "[INVALID]"
        
        print(Fore.MAGENTA + f"Cod {i + 1}: " + Fore.YELLOW + code + " " + Fore.RED + status)
        time.sleep(0.1) 

    print(Fore.CYAN + "Codurile au fost generate cu succes!")
    print(Fore.YELLOW + "\nApasa orice pt a inchide...")

    input() 

if __name__ == "__main__":
    main()
