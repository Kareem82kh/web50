from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import chromedriver_autoinstaller

# Automatically install ChromeDriver based on the installed Chrome browser version
chromedriver_autoinstaller.install()

url = 'https://submit.cs50.io/courses/1202/'
github_username = 'Kareem82kh'
github_password = 'HandsomeKareem82!!'

# Start a headless browser session using Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Optional: Run in headless mode
chrome_options.add_argument('--disable-gpu')  # Optional: Disable GPU acceleration

# Set the Chrome binary location
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# Specify the path to ChromeDriver (this is optional if using chromedriver_autoinstaller)
chromedriver_path = chromedriver_autoinstaller.install()

driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

driver.get(url)

username_input = driver.find_element_by_id('login_field')
password_input = driver.find_element_by_id('password')

username_input.send_keys(github_username)
password_input.send_keys(github_password)
password_input.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

html_source = driver.page_source

driver.quit()

soup = BeautifulSoup(html_source, 'html.parser')

paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.get_text())

links = soup.find_all('a')
for link in links:
    print(link['href'])
