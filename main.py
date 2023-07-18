from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

import json
import os

config = open('config.json', 'r')
data = json.load(config)

os.system('cls & title monkeyTyper')

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

print(banner)

options = Options()
options.page_load_strategy = 'eager'
options.add_argument(f"--user-data-dir={data['path_to_user_data']}")
options.add_argument(f'--profile-directory={data["path_to_chrome"]}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://monkeytype.com")

wait = WebDriverWait(driver, 10)

while True:
    # Find the word elements with class name "word active"
    words = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".word.active")))
    
    for word in words:
        word_text = word.get_attribute("innerText")
        actions = ActionChains(driver)
        actions.send_keys(word_text)
        actions.send_keys(' ')
        sleep(0.35) ## fastest before it detects bot usage
        actions.perform()
        sleep(0.1)
        # print(word_text)

# Close the browser
# driver.quit()