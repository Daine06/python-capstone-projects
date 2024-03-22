from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 
import requests as rq
import time

ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'
GDOCS_URL = ''#Insert your GDOCS link inside ''.

class RentalScraper:
    
    def __init__(self):
        response = rq.get(ZILLOW_URL)
        response.raise_for_status()
        website_response = response.text
        self.soup = BeautifulSoup(website_response, 'html.parser')
    
    def scrape(self):
        self.formatted_price_list = []
        scraped_prices = self.soup.find_all(class_='PropertyCardWrapper__StyledPriceLine')
        scraped_address = self.soup.select(selector='.StyledPropertyCardDataArea-anchor address')
        scraped_link = self.soup.select(selector='.StyledPropertyCardDataWrapper a')
        
        self.scraped_prices_list = [prices.getText() for prices in scraped_prices]
        self.scraped_address_list = [address.getText().strip().replace('\n','') for address in scraped_address]  
        self.scraped_link_list = [link.get('href') for link in scraped_link]
        
        for prices in self.scraped_prices_list:
            format_price = prices.replace('1 bd', '').replace('/mo', '').replace(',','').replace('+','').replace('1bd','')
            self.formatted_price_list.append(format_price)
    
    def fill_out(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option(name='detach', value=True)
        self.driver = webdriver.Edge(options=edge_options)
        
        for i in range(len(self.scraped_prices_list)):
            self.driver.get(GDOCS_URL)
            
            time.sleep(2)
            address = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(self.scraped_address_list[i])
            
            price = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(self.formatted_price_list[i])
            
            link = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(self.scraped_link_list[i])
            
            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit_button.click()
            
            time.sleep(3)
            
        self.driver.quit()