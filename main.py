from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

import json


config = open('config.json', 'r')
data = json.load(config)


banner = '''
            __,__
   .--.  .-"     "-.  .--.
  / .. \/  .-. .-.  \/ .. 
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \ '- ,\.-"`` ``"-./, -' /
   `'-' /_   ^ ^   _\ '-'`
       |  \._   _./  |
       \   \ `~` /   /
        '._ '-=-' _.'
           '~---~'

'''

Write.Print(f"{banner}", Col.DynamicMIX((Col.white, Col.yellow)), interval=0)

options = Options()
options.page_load_strategy = 'eager'
options.add_argument(f"--user-data-dir={data['path_to_user_data']}")
options.add_argument(f'--profile-directory={data["path_to_chrome"]}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://monkeytype.com")