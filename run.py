from re import X
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
from selenium.webdriver.chrome.options import Options
 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
cwd = os.getcwd()

opts = Options()
opts.headless = False
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_argument('--ignore-certifcate-errors-spki-list')
opts.add_argument("--incognito")
path_browser = f"{cwd}\chromedriver.exe"
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
def xpath_ex(el):
    element_all = wait(browser,7).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_fast(el):
    element_all = wait(browser,1).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_exs(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    element_all.send_keys(Keys.ENTER)
    
def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 

def xpath_type(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)

def login_mail():
    xpath_type('//input[@data-test="email"]',email)
    xpath_type('//input[@data-test="password"]',password)
    sleep(1)
    xpath_ex('//div[@data-test="submit"]')
    xpath_ex('//a[@class="wallet-button"]/div')
    xpath_ex('//a[text()="Desktop"]')
    xpath_ex('//div[contains(text(),"PunkWallet")]/preceding-sibling::div')
    browser.switch_to.window(browser.window_handles[1])
    xpath_long('//span[text()="OK"]/ancestor::button')
    
    verify_wallet =  wait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//div[@role="alert"]'))).text
    print(f'[*] [{email}] {verify_wallet}')
    xpath_ex('//*[@class="anticon anticon-wallet"]')
    xpath_ex('//*[text()=" Private Key"]/ancestor::button')
    sleep(2)
    private = wait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//b[text()="Private Key:"]/following-sibling::div[1]/span'))).text
    punk_address = wait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//b[text()="Private Key:"]/following-sibling::div[2]/span'))).text
    print(f"[*] [{email}] Private Key - Punk Wallet Saved!")
    with open('saved.txt','a') as f:
        f.write(f"[*] [{email}] Private Key: {private}|Punk Wallet: {punk_address}\n")
    

def open_browser(k):
    
    global browser
    global email
    global password
    data = k.split("|")
    email = data[0]
    password = data[1]
    
    random_angka = random.randint(100,999)
    random_angka_dua = random.randint(10,99)
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka}.{random_angka_dua} Safari/537.36")
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc)
    browser.get('https://pltplace.io/login')
   
    print(f"[*] [ {k} ] Login")
    
    try:
        login_mail()
    
    except Exception as e:
 
        pass
    
if __name__ == '__main__':
    global list_accountsplit
    print('[*] Automation Connect Wallet')
    print('[*] Author: RJD')
    account = open(f"{cwd}\\account.txt","r")
    list_account = account.read()
    list_account = list_account.split("\n")
    for i in list_account:
        open_browser(i)
    
  
    

    print('[*] Automation is Done')
