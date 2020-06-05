from selenium.webdriver import Firefox
from time import sleep
from string import ascii_letters
from random import choice, randint

url = 'https://www.presearch.org/'
    
def gerador():
    buscador = ''
    
    for j in range(0, randint(6, 12)):
        buscador += choice(ascii_letters)
        
    return buscador
        
Presearch = Firefox()

Presearch.get('https://www.presearch.org/')

sleep(5)

sleep(randint(2,4))

for c in range(0,31):
    buscador = gerador()
    
    Presearch.find_element_by_css_selector('#search').send_keys(buscador)
    
    sleep(randint(1,3))
    
    Presearch.find_element_by_css_selector('.btn > i:nth-child(1)').click()
    
    sleep(randint(6,9))
    
    Presearch.get(url)
    
    sleep(randint(5,8))