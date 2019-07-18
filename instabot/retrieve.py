from finder_function import read_xpath
from finder_function import read_selector

def username_from_profile():
    wait = WebDriverWait(browser, 10)
    uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, read_selector('elements','profile_username'))))
   
    return(uname)
    
def comments_on_post():
    time.sleep(2)
    return(browser.find_elements_by_xpath(read_xpath('comments','comments_on_pic')))
      
def like_button():
    wait = WebDriverWait(browser, 10)
    
    like_button = wait.until(EC.visibility_of_element_located((By.XPATH, read_xpath('like_button','like_button'))))
    return(like_button)
    
def feed_like_buttons():
    self.hearts = browser.find_elements_by_xpath("//span[@class='fr66n']")
    return(self.hearts)
    
def follower_count():
    time.sleep(1)
    return(int(browser.find_element_by_partial_link_text("followers").find_element_by_xpath('span').get_attribute('title').replace(',','')))

def following_count():
    time.sleep(1)
    return(int(browser.find_element_by_partial_link_text("following").find_element_by_xpath('span').text.replace(',','')))
    
def pics_from_profile():
    return(browser.find_elements_by_xpath(read_xpath('get_pic','all_shown')))
