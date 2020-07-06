from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
from pathlib import Path

class InvalidPathException(Exception):
    pass
def set_path(path):
    """Add path of selenium driver"""
    try:
        driver = webdriver.Chrome(path)
        driver.quit()
        file = open("drpth.txt","w")
        file.write(path)
        file.close()
    except:
        raise InvalidPathException("Cannot find driver at %s"%path)
        

def download(song, artist = None, down_path = None, play_after_downloading = True):
    """Downloads the video to given directory"""
    
    if not down_path:
        down_path = os.getcwd()
        #print(down_path)
    file = open("drpth.txt")
    dripth = file.read()
    dripth = dripth.strip()
    if artist:
        song=song+ 'by' +artist
    video=song
    chromeOptions=Options()
    chromeOptions.add_experimental_option("prefs",{"download.default_directory":down_path})
    chromeOptions.add_argument("--headless")
    driver=webdriver.Chrome(dripth,options=chromeOptions)
    wait=WebDriverWait(driver,3)
    presence = EC.presence_of_element_located   
    visible = EC.visibility_of_element_located
    driver.get("https://www.youtube.com/results?search_query=" + str(video))

    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
    print(driver.current_url)
    url=driver.current_url
    driver.get("https://ytmp3.cc/en13/")
    #driver.maximize_window()   
    driver.find_element_by_xpath("//*[@id='mp3']").click()
    driver.find_element_by_xpath("//*[@id='input']").send_keys(url)
    driver.find_element_by_xpath("//*[@id='submit']").click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="buttons"]/a[1]').click()


    '''
        chromeOptions=Options()
        chromeOptions.add_experimental_option("prefs",{"download.default_directory":down_path})
        chromeOptions.add_argument("--headless")
        driver=webdriver.Chrome(dripth,options=chromeOptions)
        driver.get("https://ytmp3.cc/en13/")
        driver.find_element_by_xpath("//*[@id='mp3']").click()
        driver.find_element_by_xpath("//*[@id='input']").send_keys(url)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="buttons"]/a[1]').click()
    '''
    old_lst = os.listdir(down_path)
    while True:
            new_lst = os.listdir(down_path)
                
            if new_lst != old_lst:
                song = set(new_lst) - set(old_lst)
                song = str(song)
                song = song.replace("{","")
                song = song.replace("}","")
                song = song.strip("'")
                
                if Path(song).suffix == '.mp3':
                    driver.quit()
                    if play_after_downloading:
                        print("Song downloaded to :"down_path)
                        print("playing")
                        os.startfile(down_path+"/"+song)
                    return "Song downloaded"
                    break


try:
    file = open("drpth.txt")

except:
    file = open("drpth.txt","w")
    print("Hello from the creator of Mudopy,Smit Parmar and Ankit Raj Mahapatra.Do report bug if any")
    print("""You must download chromedriver and call mudopy.set_path("Path to chromedriver")""")
file.close()


        
        
        
        
        
                   
    
    


