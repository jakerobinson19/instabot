from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def init_driver(file_path, headless):
  # Start browser in incognito mode to prevent cookies and disabled infobars
  options = webdriver.ChromeOptions()
  options.add_argument("incognito")
  
  if headless:
    options.add_argument("headless")
    
  driver = webdriver.Chrome(executable_path=file_path, 
                              chrome_options=options)
  driver.wait = WebDriverWait(driver, 10)
  return(driver)

def close(browser):
    browser.close()
