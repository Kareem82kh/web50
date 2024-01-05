from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import pandas as pd

chromedriver_autoinstaller.install()

url = 'https://submit.cs50.io/courses/1202/'
github_username = 'Kareem82kh'
github_password = 'HandsomeKareem82!!'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chromedriver_path = chromedriver_autoinstaller.install()

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

username_input = driver.find_element(By.ID, 'login_field')
password_input = driver.find_element(By.ID, 'password')

username_input.send_keys(github_username)
password_input.send_keys(github_password)
password_input.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

html_source = driver.page_source

driver.quit()

soup = BeautifulSoup(html_source, 'html.parser')

paragraphs = soup.find_all('p')
paragraph_texts = [paragraph.get_text() for paragraph in paragraphs]

links = soup.find_all('a')
link_hrefs = [link['href'] for link in links]

df = pd.DataFrame({'Paragraphs': paragraph_texts, 'Links': link_hrefs})

df.to_csv('cs50_results.csv', index=False)

print('Results exported to cs50_results.csv')
