from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
    driver = webdriver.Chrome()

    df = pd.read_csv("food_recipe8_urls.csv")
    recipe_urls = df.url.to_list()

    recipe_data = []
    for recipe_url in tqdm(recipe_urls[2930:]):
          
        try:
            driver.get(recipe_url)
            time.sleep(1)
        

            title=driver.find_element(By.TAG_NAME,"h1").text
            
            req=requests.get(recipe_url).content
            detail=BeautifulSoup(req,'html.parser')
            detail_element=detail.find_all('p')
            details=detail_element[1].text
            
            tags=[]
            tag_element = driver.find_elements(By.XPATH, "/html/body/div[5]/div/div[2]/div[5]/div/div[1]/div/div[1]/div/div[1]/div[11]/div[2]/div/ul/li")
            i=0
            for tag in tag_element:
                i=i+1
                tags.append(tag.find_element(By.XPATH,f"/html/body/div[5]/div/div[2]/div[5]/div/div[1]/div/div[1]/div/div[1]/div[11]/div[2]/div/ul/li[{i}]/a").get_attribute('title').removesuffix(' recipes'))
            
            recipe_data.append({
                "title": title,
                "url": recipe_url,
                "description":details,
                "types": tags
            })

            df = pd.DataFrame(data=recipe_data, columns=recipe_data[0].keys())
            df.to_csv("recipe8.1_details.csv", index=False)
        except:
            time.sleep(1)
    

   