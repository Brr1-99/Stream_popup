import subprocess
import keyboard
import time
import requests
from bs4 import BeautifulSoup

# Headers to avoid bot protection
headers=({
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
	'Accept-Language': 'en-US, en;q=0.5'
})

url = 'https://www.twitch.tv/your_streamer_url'

live = False

def main():
    global live
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    try:
        script = soup.find('script', type="application/ld+json").get_text()
        liveBroadcast = script.split(',')[-1]
        online = liveBroadcast.split('}')[0].split(':')[-1].capitalize()
    except:
        online = False

    if online == 'True':
        subprocess.Popen("Your_web_Browser_Url for example C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        time.sleep(0.5)
        keyboard.write(url)
        keyboard.press('enter')
        live = True

if __name__ == '__main__':
    while(not live):
        main()
        time.sleep(60)