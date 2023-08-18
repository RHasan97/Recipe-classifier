from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time


if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "https://eatsmarter.com/recipes/cooking/rice"
    food_urls = []
    
    for idx in tqdm(range(37)):
        
        page_no = idx + 1
        page_url = f"{base_url}?page={page_no}"
        driver.get(page_url)
        rows = driver.find_elements(By.CSS_SELECTOR, 'body > div.offset > div > div.page > div.section > div > div.panel-pane.pane-page-content > div > div > div.panel-pane.pane-eatsmarter-search-results > div > div.eatsmarter-search-results')
        for row in rows:
            for i in range(48):
                i=i+1
                url_tag = row.find_element(By.XPATH, f"/html/body/div[5]/div/div[2]/div[5]/div/div[1]/div/div/div[1]/div/div[4]/a[{i}]")
                recipe = url_tag.get_attribute('title').removesuffix('recipe')
                food_url = url_tag.get_attribute('href') 
                food_urls.append({
                    "title": recipe,
                    "url": food_url
                })
    
    df = pd.DataFrame(data=food_urls, columns=food_urls[0].keys())
    df.to_csv("food_recipe12_urls.csv", index=False)
