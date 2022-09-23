from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

with open("wordlist(1).txt") as f:
    lines = f.readlines()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('')
print ("Opened website")
sleep(1)
for i in lines:
    try:
        # pin box
        driver.find_element(By.XPATH, '//*[@id="champ-code"]').clear()
        driver.find_element(By.XPATH, '//*[@id="champ-code"]').send_keys(i[0:4])
        print (i)
        
        # Valider
        driver.find_element(By.XPATH, '//*[@id="page"]/div[7]/div/div[2]/div/div/span').click()
        sleep(.3)

        # Fermer
        driver.find_element(By.XPATH, '//*[@id="message"]/div/div/div[2]/span').click()
        sleep(.1)
    except:
        try:
            driver.find_element(By.XPATH, '//*[@id="page"]/div[7]/div/div[1]/span')
        except:
            break
        try:
            driver.find_element(By.XPATH, '//*[@id="message"]/div/div/div[2]/span').click()
        except:
            pass
input(f'Done! Key found: {i}')
