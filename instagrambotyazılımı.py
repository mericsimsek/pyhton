from instauserinfo import username,password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
class Instagram:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password


    def signin(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        usernameinput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordinput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')

        usernameinput.send_keys(self.username)
        passwordinput.send_keys(self.password)
        passwordinput.send_keys(Keys.ENTER)
        time.sleep(6)

    def getfollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
        followlink=self.browser.find_element(By.XPATH,'//*[@id="mount_0_0_zv"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/span').click()
        time.sleep(3)
        followers=self.browser.find_element(By.CSS_SELECTOR,'div[role=dialog] ul').find_element(By.CSS_SELECTOR,'li')
        
        for user in followers:
            link=user.find_element(By.CSS_SELECTOR,"a".__getattribute__("href"))
            print(link)

insta=Instagram(username,password)
insta.signin()
insta.getfollowers()