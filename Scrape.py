from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import requests
import pandas as pd


#Provided a path for the chrome driver
executable_path ={'executable_path':r'C:\Users\sunandan\Downloads\chromedriver_win32\chromedriver.exe'}
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
browser = Browser('chrome',**executable_path,headless=False,options=options)
browser.visit('https://www.eia.gov/petroleum/')
Table = pd.read_html("https://www.eia.gov/petroleum/")
Table_df = Table[0]
Table_df.to_html("Table.html")
Heading = browser.find_by_css('table[class="basic_table"]').find_by_tag('caption').text