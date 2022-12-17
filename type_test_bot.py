from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import keyboard

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.livechat.com/typing-speed-test/#/')
print ("Opened website")
sleep(1)

keyboard.wait('enter')
while not driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[1]/div/div[1]/div/div[1]').text == '0':
    content = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]')
    keyboard.write(f'{content.text} ')
    sleep(.1)
input("Press enter")
