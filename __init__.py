from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from bs4 import BeautifulSoup
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
    url=get_url(song,artist)
        
    if url:
        if not down_path:
            down_path = os.getcwd()
        file = open("drpth.txt")
        dripth = file.read()
        dripth = dripth.strip()
        chromeOptions=Options()
        chromeOptions.add_experimental_option("prefs",{"download.default_directory":down_path})
        #chromeOptions.add_argument("--headless")
        driver=webdriver.Chrome(dripth,options=chromeOptions)
        driver.get("https://ytmp3.cc/en13/")
        driver.find_element_by_xpath("//*[@id='mp3']").click()
        driver.find_element_by_xpath("//*[@id='input']").send_keys(url)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="buttons"]/a[1]').click()
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
                        print("playing")
                        os.startfile(down_path+"/"+song)
                    return "Song downloaded"
                    break
    
def get_url(song, artist = None):
    """Get url to the video with following song name"""
    if artist:
        song = song+" by "+artist
        print(song)
    song = song.replace(" ","%20")
    try:
        url = 'https://www.youtube.com/results?q=' + song
        print(url)
        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
        sc = requests.get(url)
        time.sleep(1)
        sctext = sc.text
        time.sleep(1)
        soup = BeautifulSoup(sctext)
        songs = soup.findAll("div",{"class":"yt-lockup-video"})
        song = songs[0].contents[0].contents[0].contents[0]
        songurl = song["href"]
        url = "https://www.youtube.com"+songurl
        return(url)
    except Exception as e:
        print("url not found", e,"Try adding more lysics or Artist name")

try:
    file = open("drpth.txt")

except:
    file = open("drpth.txt","w")
    print("Hello from the creator of <add name here>, do reposrt bug if any")
    file.close()


        
        
        
        
        
                   
    
    


