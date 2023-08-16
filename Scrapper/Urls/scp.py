from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time


if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "https://www.imdb.com/search/keyword/?mode=advanced&"
    film_urls = []
    
    for idx in tqdm(range(124)):
        page_no = idx + 101
        page_url = f"{base_url}?page={page_no}&title_type=movie&ref_=kw_nxt&sort=user_rating,desc"
        driver.get(page_url)
        rows = driver.find_elements(By.CSS_SELECTOR, '#main > div > div.lister.list.detail.sub-list > div.lister-list')
        for row in rows:
            for i in range(49):
                i=i+1
                url_tag = row.find_element(By.XPATH, f"//*[@id='main']/div/div[2]/div[3]/div[{i}]/div[3]/h3/a")
                feature_film = url_tag.text 
                film_url = url_tag.get_attribute('href')
                film_urls.append({
                    "title": feature_film,
                    "url": film_url
                })
            
                time.sleep(5)
   
   
    df = pd.DataFrame(data=film_urls, columns=film_urls[0].keys())
    df.to_csv("feature_film_urls.csv", index=False)