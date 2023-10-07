import requests
from selenium import webdriver
import time 
from instauserinfo import email,password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class twitter:
    def __init__(self,email,password):
        self.browserprofile=webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser=webdriver.Chrome('chromedriver.exe',chrome_options=self.browserprofile)
        self.email=email
        self.password=password

    def signin(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        emailinput=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        passwordinput=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')

        emailinput.send_keys(self.email)
        passwordinput.send_keys(self.password)

        button=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]').click()
        time.sleep(2)


    def search(self,hastag):
        searchinput=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        searchinput.send_keys(hastag)
        time.sleep(3)
        searchinput.send_keys(Keys.ENTER)
        time.sleep(3)

        
        last_height=self.browser.execute_script("return document.documentElement.scrollHeight")#java script komutu aktif ediyo bu doc.el. komutu sayfanın en aşağısına indiriyor
        while True:
            if loopcounter>3:#3 kere en aşağı iner tüm tweetleri yazdırır
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            time.sleep(3)
            new_height=self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height==new_height: #eğer eşit olmazsa ynei tweet gelmiş demek
                break
            last_height=new_height
            loopcounter+=1
        list=self.browser.find_elements(By.XPATH,'//div[@data-testid="tweet"]/div[1]/div[1]/div[2]/div[4]/div[1]')#bu div 1 1 2 4 1 ben kendim yazdım data testid den itibaren aşşağı doğru açık olanları yazdıl
        for item in list:
            print(item.text)

twtr=twitter(email,password)
twtr.signin()