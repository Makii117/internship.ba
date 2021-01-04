from selenium import webdriver
from selenium.webdriver.chrome.options import Options




# Initialize webdriver
#SET FUCKING PATH AND PROPER CHROME VERSIONS
path = r'./'
driver=webdriver.Chrome()
print(driver.capabilities['version'])
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
driver = webdriver.Chrome(executable_path = path,chrome_options=options)

driver.get("google.com")


#Scrape web for relevant info (general info for SA)


# Get urls for scraping



#Scrape pages for information



#Export information to database



