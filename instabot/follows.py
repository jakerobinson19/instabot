

def get_following_status():

def unfollow_user(self, user):
    self.goToProfile(user)
    follow_button = self.browser.find_element_by_xpath('//button[text()="Following"]')
    follow_button.click()

    confirm = confirm = browser.find_element_by_xpath('//button[text()="Unfollow"]')
    confirm.click()
