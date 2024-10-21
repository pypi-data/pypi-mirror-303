from colorama import Fore, Style

class banner:
    def __init__(self):
        self.blue = Fore.BLUE
        self.green = Fore.GREEN
        self.red = Fore.RED
        self.yellow = Fore.YELLOW
        self.white = Fore.WHITE
        self.reset = Style.RESET_ALL

    def create_banner(self, game_name: str):
        # Create banner with game name
        banner = f"""
{Fore.CYAN}┏━━━━━━━━━━━━━━━━┓
┃{self.blue}╭━┳━╭━╭━╮╮      {Fore.CYAN}┃   {self.red}ＡＣＣＯＵＮＴ{Fore.CYAN}
┃{self.blue}┃┈┈┈┣▅╋▅┫┃      {Fore.CYAN}┣━━━━━━━━━━━━━━━━━━━━━┓
┃{self.blue}┃┈┃┈╰━╰━━━━━━╮  {Fore.CYAN}┃{self.green}TELEGRAM > @FoxZenon{Fore.CYAN}
┃{self.blue}┃╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣{Fore.CYAN}┗━━━━━━━━━━━━━━━━━━━━━┛
┃{self.blue}┃╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉{Fore.CYAN}┃{self.green} GITHUB  > foxZenonn {Fore.CYAN}
┃{self.blue}┃╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤{Fore.CYAN}┏━━━━━━━━━━━━━━━━━━━━━┓
┃{self.blue}┃╲┃┈┈┈┈╭━┳━━━━╯ {Fore.CYAN}┃ {self.green}CODER   >  Zannn   {Fore.CYAN}
┃{self.blue}┃╲┣━━━━━━┫      {Fore.CYAN}┣━━━━━━━━━━━━━━━━━━━━━┛
┗━━━━━━━━━━━━━━━━┛{self.reset}
{self.yellow}Group  {self.white}https://t.me/zenonnfox{self.reset}
{self.yellow}GAME  {self.red}{game_name}{self.reset}
"""
        return banner

banner = banner()