from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os



import urllib

def videoDownloader(videoUrl):
    name = (videoUrl.split(".")[-2]).replace("/", "")
    filename=name+".mp4"
    cwd = os.getcwd()
    path = cwd+"/downloads/videos/"
    fullpath = os.path.join(path, filename)
    try:
        print("starts Downloading :"+videoUrl +"...\n")
        print("download to :"+fullpath)
        urllib.request.urlretrieve(videoUrl, fullpath)
        print("Download completed..!!")
    except Exception as e:
        print(e)

def facebookLiveDownloader(url):
    usr = "jo06942@gmail.com"
    pwd = "facebook0845916998Ntsd"
    webDriver = webdriver.Chrome()
    webDriver.get(url)
    elem = webDriver.find_element_by_name("email")
    elem.send_keys(usr)
    elem = webDriver.find_element_by_name("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)

    wait = WebDriverWait(webDriver, 10)

    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'widePic'))
        wait.until(element_present)
    except:
        print("login too long")
    while 1:
        videoBox = webDriver.find_element_by_class_name("widePic")
        videoBox.click()
        print("click play video")
        try:
            element_present = EC.presence_of_element_located((By.ID, 'mInlineVideoPlayer'))
            wait.until(element_present)
            videoUrl = webDriver.find_element_by_id('mInlineVideoPlayer').get_property("src")
            print("Video url is ready! at :"+videoUrl)
            videoDownloader(videoUrl)
            break
        except:
            print("Loading took too much time!")

        webDriver.refresh()



if __name__ == '__main__':
    facebookLiveDownloader("https://m.facebook.com/groups/520603828139097/permalink/677999315732880/")