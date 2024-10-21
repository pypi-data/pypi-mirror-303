import os
import sys
from colorama import *
import json
from datetime import datetime
import requests
from requests.auth import HTTPProxyAuth

# Inisialisasi colorama
init(autoreset=True)

# Kode ANSI untuk warna
RESET = "\033[0m"
COLORS = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "BLACK": "\033[30m",
    "LIGHT_RED": "\033[91m",
    "LIGHT_GREEN": "\033[92m",
    "LIGHT_YELLOW": "\033[93m",
    "LIGHT_BLUE": "\033[94m",
    "LIGHT_MAGENTA": "\033[95m",
    "LIGHT_CYAN": "\033[96m",
    "LIGHT_WHITE": "\033[97m"
}

class Base:
    def __init__(self):
        # Inisialisasi colorama styles
        self.red = Fore.LIGHTRED_EX
        self.yellow = Fore.LIGHTYELLOW_EX
        self.green = Fore.LIGHTGREEN_EX
        self.black = Fore.LIGHTBLACK_EX
        self.blue = Fore.LIGHTBLUE_EX
        self.white = Fore.LIGHTWHITE_EX
        self.reset = Style.RESET_ALL

    def file_path(self, file_name: str):
        # Mendapatkan direktori file yang memanggil metode ini
        caller_dir = os.path.dirname(
            os.path.abspath(sys._getframe(1).f_code.co_filename)
        )
        file_path = os.path.join(caller_dir, file_name)
        return file_path

    def create_line(self, length: int):
        # Membuat garis berdasarkan panjang
        line = self.white + "~" * length
        return line

    def create_banner(self, game_name: str):
        # Ganti dengan banner tambahan yang telah dibuat
        banner_tambahan = f"""
        {COLORS['CYAN']}┏━━━━━━━━━━━━━━━━┓
        ┃{COLORS['BLUE']}╭━┳━╭━╭━╮╮      {COLORS['CYAN']}┃   {COLORS['RED']}ＡＣＣＯＵＮＴ{COLORS['CYAN']}
        ┃{COLORS['BLUE']}┃┈┈┈┣▅╋▅┫┃      {COLORS['CYAN']}┣━━━━━━━━━━━━━━━━━━━━━┓
        ┃{COLORS['BLUE']}┃┈┃┈╰━╰━━━━━━╮  {COLORS['CYAN']}┃{COLORS['MAGENTA']}TELEGRAM > @FoxZenon{COLORS['CYAN']} ┃
        ┃{COLORS['BLUE']}┃╰┳╯┈┈┈┈┈┈┈┈◢▉◣{COLORS['CYAN']}┗━━━━━━━━━━━━━━━━━━━━━┛
        ┃{COLORS['BLUE']}┃╲┃┈┈┈┈┈┈┈┈┈▉▉▉{COLORS['CYAN']}┃{COLORS['MAGENTA']} GITHUB  > foxZenonn {COLORS['CYAN']}┃
        ┃{COLORS['BLUE']}┃╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤{COLORS['CYAN']}┏━━━━━━━━━━━━━━━━━━━━━┓
        ┃{COLORS['BLUE']}┃╲┃┈┈┈┈╭━┳━━━━╯ {COLORS['CYAN']}┃ {COLORS['MAGENTA']}CODER   >  Zannn   {COLORS['CYAN']} ┃
        ┃{COLORS['BLUE']}┃╲┣━━━━━━┫      {COLORS['CYAN']}┣━━━━━━━━━━━━━━━━━━━━━┛
        ┗━━━━━━━━━━━━━━━━┛{RESET}
        {game_name}"""
        return banner

    def get_config(self, config_file: str, config_name: str):
        # Mendapatkan konfigurasi dari file konfigurasi
        config_status = (
            json.load(open(config_file, "r")).get(config_name, "false"). lower()
            == "true"
        )
        return config_status

    def clear_terminal(self):
        # Untuk Windows
        if os.name == "nt":
            _ = os.system("cls")
        # Untuk macOS dan Linux
        else:
            _ = os.system("clear")

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{self.black}[{now}]{self.reset} {msg}{self.reset}")

    # Format proxy
    def format_proxy(self, proxy_info):
        return {"http": f"{proxy_info}", "https": f"{proxy_info}"}

    def check_ip(self, proxy_info):
        url = "https://api.ipify.org?format=json"
        proxies = self.format_proxy(proxy_info=proxy_info)

        if "@" in proxy_info:
            proxy_credentials = proxy_info.split("@")[0]
            proxy_user = proxy_credentials.split(":")[1]
            proxy_pass = proxy_credentials.split(":")[2]
            auth = HTTPProxyAuth(proxy_user, proxy_pass)
        else:
            auth = None

        try:
            response = requests.get(url=url, proxies=proxies, auth=auth)
            response.raise_for_status()  # Menaikkan kesalahan untuk kode status yang buruk
            actual_ip = response.json().get("ip")
            self.log(f"{self.green}Actual IP Address: {self.white}{actual_ip}")
            return actual_ip
        except requests.exceptions.RequestException as e:
            self.log(f"{self.red}IP check failed: {self.white}{e}")
            return None

    def parse_proxy_info(self, proxy_info):
        try:
            stripped_url = proxy_info.split("://", 1)[-1]
            credentials, endpoint = stripped_url.split("@", 1)
            user_name, password = credentials.split(":", 1)
            ip, port = endpoint.split(":", 1)
            self.log(f"{self.green}Input IP Address: {self.white}{ip}")
            return {"user_name": user_name, "pass": password, "ip": ip , "port": port}
        except:
            self.log(
                f"{self.red}Check proxy format: {self.white}http://user:pass@ip:port"
            )
            return None

# Membuat objek Base
base = Base()