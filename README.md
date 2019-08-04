# instabot

There are several instagram bots available on Github, this one is tailored to the goal of follower growth by applying Gary Vaynerchuks $1.80 strategy of commenting on approximately 90 unique accounts everyday. This bot takes the strategy one step further by also liking several of the past photos for accounts that are commented on. However, while a key part of the $1.80 strategy is using comments related to the pictures content, this automated bot can only allow limited customization of comments.

The user will be able to specify the rules of engagement including how many accounts to view, how many pictures of each account to like or comment on, and if and what to comment on pictures.

# Requirements

This bot is written in python and requires the use of the web browser automation tool, Selenium.

To install Selenium, enter the commands below (based on your operation system):

#### Windows:
pip install selenium

#### MacOS:
sudo easy_install selenium

### Install drivers:

Selenium requires a web driver to access the latest and greatest features. For the bot to work, you should download the webdriver for the browser that you plan to use and, once downloaded, add the driver to your $PATH by putting it in your */usr/local/bin* or */usr/bin* directories (depending on where Python is installed). 

For a full list of drivers to download for Selenium, go to: https://www.seleniumhq.org/download/

Otherwise, here are links to the most popular drivers.

| Browser        | Link                                                        |
|---|---|
| Chrome         | https://sites.google.com/a/chromium.org/chromedriver/       |
| Firefox        | https://github.com/mozilla/geckodriver/                     |

Note: to see the version of the browser you have go to Settings>About Chrome or Menu>Help>About FireFox






