from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from multiprocessing.pool import ThreadPool
import time
pl = []
prolist = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all").text
prolist1 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all").text
prolist2 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all").text
dl = []
my_url = "https://www.youtube.com/watch?v=Az-SIHZhzgc&list=PLZzMHROnvDL_qhylK7TOLgbRSc7ROwwAO&index=1"

def tri(i):
   try:
    if requests.get(my_url,proxies={"https":"https://"+i},timeout=1).status_code == 200:
       print (i)
       pl.append(i)
       tro(i)
   except:
    pass

def tro(i):
            chrome_options = Options()
            chrome_options.add_argument("--proxy-server="+i)    
            driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)
            driver.get("https://youtube.com/c/rezondegrowtopia")
            driver.get(my_url)
            if not "pause" in driver.page_source or "Play" in driver.page_source:
               driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[25]/div[2]/div[1]/button").click()
            dl.append(driver)

tp = ThreadPool(5000)
tp.map(tri,prolist.splitlines())
tp.map(tri,prolist1.splitlines())
tp.map(tri,prolist2.splitlines())
for i in dl:
    i.minimize_window()

while True:
    for i in dl:
        if "Play" in driver.page_source:
            driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[25]/div[2]/div[1]/button").click()
