import requests
from selenium import webdriver
import time 
from instauserinfo import email,password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class github:
    def __init__(self,email,password):
        self.browser=webdriver.Chrome()
        self.email=email
        self.password=password
        self.followers=[]

    def signin(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)
        
        self.browser.find_element(By.XPATH,'//*[@id="login_field"]').send_keys(self.email)
        self.browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(self.password)

        time.sleep(2)

        button=self.browser.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[12]').click()

    def loadfollowers(self):
        items=self.browser.find_elements(By.CSS_SELECTOR,'.d-table.table-fixed ')

        for i in items:
          self.followers.append( i.find_element(By.CSS_SELECTOR,'.Link--secondary.pl-1').text)#
    def getfollowers(self):
        self.browser.get("https://github.com/mericsimsek?tab=following")
        time.sleep(3)

        
        
        while True:
            links=self.browser.find_element(By.CLASS_NAME,("pagination")).find_elements(By.TAG_NAME,'a')
#next ve previus 2 tane div olduğu için bunların bağlı olduğunu classı aldık sadece nextleme mıuhabbeti olsa direkt nextin xpathini alırdık da 
#next diyince 2.sayfada previus ta aktif oluyor bundan dolayı 2 tane a nın classını aldık ve tag name olarak a larını yazdırdık
            if len(links)==1:
                if links[0].text=="Next":#0.index dediği ilk a tagnamei alıyor yani next
                    links[0].click()#burada 1.sayfada next diyip 2.sayfaya geçiş yapıyorz
                    time.sleep(1)

                    self.loadfollowers()
                else:
                    break
            else:
                for link in links: #next değilse continue diyip bir sonraki döngğden devam eder
                    if link.text =="Next":
                        link.click()
                        time.sleep(1)

                        self.loadfollowers()
            

githb=github(email,password)
githb.signin()
githb.getfollowers()
print(githb.followers)
print(len(githb.followers))#kaç tane geldiğine bakılır