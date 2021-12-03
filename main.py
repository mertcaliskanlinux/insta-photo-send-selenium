from selenium import webdriver
from selenium.webdriver.common.by import By
from id_pas import username,password
import time





class Instagram():

        def __init__(self,username,password):
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0")

            driver = webdriver.Firefox(firefox_profile=profile,executable_path="/home/mert/Desktop/sanal_ortam/geckodriver") #SİZİN WEBDRİVER DOSYA YOLUNUZ
            username = username
            password = password

            driver.get("https://www.instagram.com/")
            time.sleep(4)
            driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
            time.sleep(5)
            driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
            login = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
            time.sleep(5)
            login.click()
            time.sleep(5)
            driver.get("https://www.instagram.com/")
            time.sleep(5)
            notNow = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/button[1]")
            time.sleep(5)
            notNow.click()
            time.sleep(5)
            driver.get("https://www.instagram.com/{}/".format(username))
            time.sleep(5)
            while True:
                profile_btn = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/div/div/div/button")
                time.sleep(5)
                profile_btn.click()
                time.sleep(5)
                s = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/form/input")
                time.sleep(3)
                s.send_keys("/home/mert/Desktop/sanal_ortam/1.jpg")#SİZİN DOSYA YOLUNUZ
                time.sleep(5)
                profile_btn = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/div/div/div/button")
                time.sleep(5)
                profile_btn.click()
                time.sleep(5)
                s = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/form/input")
                time.sleep(3)
                s.send_keys("/home/mert/Desktop/sanal_ortam/2.jpg") #SİZİN DOSYA YOLUNUZ
                time.sleep(5)
                profile_btn = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/div/div/div/button")
                time.sleep(5)
                profile_btn.click()
                time.sleep(5)
                s = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/form/input")
                time.sleep(3)
                s.send_keys("/home/mert/Desktop/sanal_ortam/3.jpg")#SİZİN DOSYA YOLUNUZ
                time.sleep(5)
                profile_btn = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/div/div/div/button")
                time.sleep(5)
                profile_btn.click()
                time.sleep(5)
                s = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[2]/form/input")
                time.sleep(3)
                s.send_keys("/home/mert/Desktop/sanal_ortam/4.jpg")#SİZİN DOSYA YOLUNUZ
                time.sleep(5)


Instagram(username,password)

        


        







