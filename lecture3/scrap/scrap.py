from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Replace 'YOUR_URL_HERE' with the actual URL of the page containing your data
url = 'https://submit.cs50.io/courses/1202/'

# Replace 'YOUR_GITHUB_USERNAME' and 'YOUR_GITHUB_PASSWORD' with your GitHub credentials
github_username = 'Kareem82kh'
github_password = 'HandsomeKareem82!!'

# Specify the path to ChromeDriver
chromedriver_path = '/path/to/chromedriver'  # Replace with the actual path to Chromedriver

# Specify the path to the Google Chrome executable
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# Start a headless browser session using Selenium
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=webdriver.ChromeOptions().binary_location(chrome_path))

# Open the URL
driver.get(url)

# Locate the login elements and fill in your GitHub credentials
username_input = driver.find_element_by_id('login_field')
password_input = driver.find_element_by_id('password')

username_input.send_keys(github_username)
password_input.send_keys(github_password)

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the page to load after login (adjust sleep time if needed)
driver.implicitly_wait(5)

# Get the page source after login
html_source = driver.page_source

# Close the browser
driver.quit()

# Continue with BeautifulSoup to parse the HTML source
soup = BeautifulSoup(html_source, 'html.parser')

# Extract relevant information based on the HTML structure
# Modify this part according to the actual HTML structure of the page

# Example: Extract all text from paragraph tags
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.get_text())

# Example: Extract all links
links = soup.find_all('a')
for link in links:
    print(link['href'])
