

def get_following_status(browser):
    status = browser.find_element_by_xpath(read_xpath('get_following_status','follow_button_XP').text
    if status == 'Following':
      print('We are already following this user')
    elif status == 'Follow Back':
      print('This user follows us but we do not follow back')
    elif status == 'Requested':
      print('We have already requested to follow this user')
    else:
      print('We do not follow this user')
    
def unfollow_user(self, user):
    self.goToProfile(user)
    follow_button = self.browser.find_element_by_xpath('//button[text()="Following"]')
    follow_button.click()

    confirm = confirm = browser.find_element_by_xpath('//button[text()="Unfollow"]')
    confirm.click()
