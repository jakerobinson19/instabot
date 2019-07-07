



def rightArrow(self):
    self.body = self.browser.find_element_by_tag_name('body')
    self.body.send_keys(Keys.ARROW_RIGHT)

def leftArrow(self):
    self.body = self.browser.find_element_by_tag_name('body')
    self.body.send_keys(Keys.ARROW_LEFT)
