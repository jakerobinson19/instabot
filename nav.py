#!/usr/bin/env python



def right_arrow():
    self.body = self.browser.find_element_by_tag_name('body')
    self.body.send_keys(Keys.ARROW_RIGHT)

def left_arrow():
    self.body = self.browser.find_element_by_tag_name('body')
    self.body.send_keys(Keys.ARROW_LEFT)

def go_to_profile(uname = None):
    if uname == None:
        uname = self.email
    self.browser.get('https://www.instagram.com/{}'.format(uname))
  
def get_username():
    wait = WebDriverWait(self.browser, 10)
    uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.BrX75')))
    return(uname)

def go_to_hashtag(hashtag):
    self.browser.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
  
