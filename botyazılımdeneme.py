from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome()

url="https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=451050238842-stelcbipu0o33seaasv3sd3gt8ktilti.apps.googleusercontent.com&redirect_uri=https%3A%2F%2F10fastfingers.com%2Faccount%2Fgoogle_oauth2callback&state&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&approval_prompt=auto&service=lso&o2v=2&flowName=GeneralOAuthFlow"
browser.get(url)

alan=browser.find_element(By.CSS_SELECTOR,'[name="identifier"]')#burada  email yazın yere sağ tıkladık
time.sleep(1)

alan.send_keys("mericsimsek344@gmail.com")
time.sleep(2)

button=browser.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span')#istersen xpath ister name ile yazdırabilirsin bi üstteki gibi
button.click()#tamamen tercihine bağlı xpath daha kolay by.xpath yazıp name... yerine yine id... yazacan 

time.sleep(1)#button için sonrakiye sağ tıklayıp inceledim yukarıdaki xpathı kopyaladım tıklama komudu için click verdim

browser.get("https://10fastfingers.com/typing-test/turkish")#klavye hız testine gçeiş yapıyor
time.sleep(2)


i=1
inputa=browser.find_element(By.XPATH,'//*[@id="inputfield"]')#burası sitedeki o boş yere kelimeleri gireceği yer input alanı yani 
while i<200:
    kelime=browser.find_element(By.XPATH,'//*[@id="row1"]/span["+str(i)+"]')
i+=1
inputa.send_keys(kelime.text)
time.sleep(0.1)