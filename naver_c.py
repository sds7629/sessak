import requests
import time
import pandas as pd
import aiohttp
import asyncio
from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://comic.naver.com/api/article/list?titleId=769209"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

session = requests.Session()
res = session.get(url, headers=headers)

title_list = []
urls = []

async def fetch(session, url):
    async with session.get(url) as res:
        return await res.text()


async def craw_get():
    async with aiohttp.ClientSession() as session:
        res = await fetch(session, url)
        if res:
            soup = BeautifulSoup(res, "html.parser")
            titles = soup.select(".sa_text_title")

            for title in titles:
                urls.append(title["href"])
                title_list.append(title.text.strip("\n"))

            df = pd.DataFrame()
            df["url"] = urls
            df["제목"] = title_list
            print(df)

        else:
            print("bi")


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(craw_get())
#     try:
#         start = time.time()
#         loop.run_until_complete(task)
#         end = time.time()
#         print(end - start)
#     except KeyboardInterrupt:
#         print("Command + c")
#     loop.close()

if res:
    start = time.time()
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.find("a", {"class": "EpisodeListList__link--DdClU"}))

    # for title in titles:
    #     print(title["subtitle"])
    # df = pd.DataFrame()
    # df["url"] = urls
    # df["제목"] = title_list
    # print(df)
    # end = time.time()
    # print(end - start)
else:
    print("bi")
