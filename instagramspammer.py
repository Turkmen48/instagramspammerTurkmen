from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import itertools
class Instaspam:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browserprofile=webdriver.ChromeOptions()
        self.browserprofile.add_experimental_option('prefs',{'intl.accpet_languages':'en,en_US'})
        self.browser=webdriver.Chrome('chromedriver.exe',chrome_options=self.browserprofile)
    def giris(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        login=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
        password=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        button=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
        login.send_keys(self.username)
        password.send_keys(self.password)
        button.click()
    def spam(self,kurban):
        self.giris()
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{kurban}") #kurbanın adını yaz
        time.sleep(3)
        ucnokta=self.browser.find_element_by_class_name("_8-yf5")
        ucnokta.click()
        time.sleep(1)
        report=self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/button[3]")
        report.click()
        time.sleep(1)
        spam=self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]")
        spam.click()
        time.sleep(1)
        self.browser.close()
print("""
Bu program Turkmen tarafından kodlandı. 
Made by Turkmen
""")
with open("kullanicilar.txt") as f:
    kullanici_adlari = f.readlines()
kullanici_adlari = [x.strip() for x in kullanici_adlari]
with open("sifreler.txt") as s:
    sifreler = s.readlines()
sifreler = [y.strip() for y in sifreler]

sayac=1
kullanici_sayisi=len(kullanici_adlari)
kurban=input("spamlayacağınız kişinin kullanıcı adı?")
while sayac<=kullanici_sayisi:
    for k,p in zip(kullanici_adlari,sifreler):
        instaspam = Instaspam(k,p)
        instaspam.spam(kurban)
        sayac+=1

print(f"Spam işlemi tamamlandı. Toplam {kullanici_sayisi} kere spamlandı. ")




