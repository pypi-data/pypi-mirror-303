from colorama import Fore, Style

class banner:
    def __init__(self):
       # Initialize colorama styles
        self.red = Fore.LIGHTRED_EX
        self.yellow = Fore.LIGHTYELLOW_EX
        self.green = Fore.LIGHTGREEN_EX
        self.black = Fore.LIGHTBLACK_EX
        self.blue = Fore.LIGHTBLUE_EX
        self.white = Fore.LIGHTWHITE_EX
        self.cyan = Fore.LIGHTCYAN_EX
        self.magenta = Fore.LIGHTMAGENTA_EX
        self.reset = Style.RESET_ALL

    def create_banner(self, game_name: str):
        # Create banner with game name
        banner = f"""
 {self.cyan}
\n\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  {self.white}ZENON FOX {self.red}✚{self.white} MINIAPP BOT {self.cyan}┃         {self.white}COPYRIGHT BY Zennon{self.cyan}
┣━━━━━━━━━━━━━━━━━━━━━━━━━━┫  {self.white}⟨⟨⟨{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.white}⟩⟩⟩{self.cyan}
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀ {self.cyan}┃     {self.blue} GITHUB    {self.cyan}➤ {self.white}github.com/foxZenonn{self.cyan}
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠙⠻⢶⣄⡀⠀⠀⠀⢀⣤⠶⠛⠛⡇ {self.cyan}┃
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⣙⣿⣦⣤⣴⣿⣁⠀⠀⣸⠇ {self.cyan}┃      {self.blue}TG OWNER  {self.cyan}➤{self.white} t.me/FoxZenon{self.cyan}
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣿⣿⣿⣿⣿⣷⣌⠋⠀ {self.cyan}┃⠀
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⡈⢻⣿⡟⢁⣠⣾⣿⣦⠀ {self.cyan}┃      {self.blue}TG GROUP  {self.cyan}➤{self.white} t.me/zzenonFox{self.cyan}
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠘⣿⠃⣿⣿⣿⣿⡏⠀ {self.cyan}┃  {self.white}⟨⟨⟨{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.white}⟩⟩⟩{self.cyan}
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠛⣰⠿⣆⠛⠁⠀⡀⠀⠀ {self.cyan}┃             {self.white}YOUR PLAY GAME{self.cyan}
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣦⠀⠘⠛⠋⠀⣴⣿⠁⠀⠀ {self.cyan}┃  {self.white}⟨⟨⟨{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.white}⟩⟩⟩{self.cyan}
┃{self.yellow}⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣏⠀⠀ ⠀{self.cyan}┃      {self.blue}GAME{self.cyan} ➤{self.white} {game_name}
┃{self.yellow}⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠀⠀⠀⠾⢿⣿⠀⠀ ⠀{self.cyan}┃            {self.red}●   {self.yellow}●   {self.blue}●   {self.white}●   {self.cyan}
┃{self.yellow}⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠟⠋⣁⣠⣤⣤⡶⠶⠶⣤⣄⠈⠀⠀ ⠀{self.cyan}┃          ┏━━━━━━━━━━━━━━━┓
┃{self.yellow}⠀⢰⣿⣿⣮⣉⣉⣉⣤⣴⣶⣿⣿⣋⡥⠄⠀⠀⠀⠀⠉⢻⣄⠀ ⠀{self.cyan}┃          ┃{self.magenta}╔═╗╔═╗╔╗╔╔═╗╔╗╔{self.cyan}┃
┃{self.yellow}⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣁⣤⣀⣀⣤⣤⣤⣤⣄⣿⡄⠀ {self.cyan}┃          ┃{self.magenta}╔═╝║╣ ║║║║║║║║║{self.cyan}┃
┃{self.yellow}⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠛⠃⠀ {self.cyan}┃          ┃{self.magenta}╚═╝╚═╝╝╚╝╚═╝╝╚╝{self.cyan}┃
┃{self.yellow}⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {self.cyan}┃          ┗━━━━━━━━━━━━━━━┛
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛  {self.white}⟨⟨⟨{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.blue}━{self.red}━{self.white}━{self.yellow}{self.red}━{self.white}━{self.yellow}━{self.green}━{self.magenta}━{self.black}━{self.white}⟩⟩⟩{self.cyan}
  {self.reset}
"""
        return banner

banner = banner()