<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#simple-instagram-bot)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Configuration](#configuration)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## Simple Instagram Bot
-----------------------
There are several instagram bots available on Github, this one is tailored to the goal of follower growth by applying Gary Vaynerchuks $1.80 strategy of commenting on approximately 90 unique accounts everyday. This bot takes the strategy one step further by also liking several of the past photos for accounts that are commented on. However, while a key part of the $1.80 strategy is using comments related to the pictures content, this automated bot can only allow limited customization of comments.

The user will be able to specify the rules of engagement including how many accounts to view, how many pictures of each account to like or comment on, and if and what to comment on pictures.

The general workflow for the bot is as follows:
1. Go to a hashtag discover page (permitted hashtags are configurable)
2. Comment on a number of accounts on the discover page
3. Go to each account and like a set number of past pictures
4. Repeat periodically until comment or likes limit reached (as per configuration)

### Built With
* [Python 3.7](https://www.python.org/downloads/)
* [Selenium](http://www.seleniumhq.org/download/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- This code was written using [Python 3.7](https://www.python.org/downloads/).
- [Selenium](http://www.seleniumhq.org/download/) (this can be PIP installed, written using v3.0.2).
- The Selenium package requires a webdriver program. This code was written 
using [Chromedriver](https://chromedriver.storage.googleapis.com/index.html) v78.

Refer to and install the requirements.txt for all dependencies
```sh
pip install requirements.txt
```

### Installation
#### Windows:
```sh
pip install selenium
```
#### MacOS:
```sh
sudo easy_install selenium
```
#### Install drivers:

Selenium requires a web driver to access the latest and greatest features. For the bot to work, you should download the webdriver for the browser that you plan to use and, once downloaded, add the driver to your $PATH by putting it in your */usr/local/bin* or */usr/bin* directories (depending on where Python is installed). 

For a full list of drivers to download for Selenium, go to: https://www.seleniumhq.org/download/

Otherwise, here are links to the most popular drivers.

| Browser        | Link                                                        |
|---|---|
| Chrome         | https://sites.google.com/a/chromium.org/chromedriver/       |
| Firefox        | https://github.com/mozilla/geckodriver/                     |

Note: to see the version of the browser you have go to Settings>About Chrome or Menu>Help>About FireFox

### Configuration
Set the basic parameters for access and engagement in the config.py file

1. Set the username and password for the account you want the bot to run on.
```sh
USERNAME = <ig_username>
PASSWORD = <ig_password>
```

2. Set the limit on the number of likes/comments you would like to perform during the session. The bot will stop running once either of these conditions are met. 
```sh
MAX_LIKES = 300
MAX_COMMENTS = 55
```
 * Note: Although you are free to set the limit to almost infinity to let the bot run indefinitely, Instagram will likely catch on and block the account. For this reason a limit was set such that the bot will stop and you can choose to reintitiate later. 

3. Set the number of profiles to interact with per hashtag you visit (PROFILES_PER_TAG), as well as how many pictures you want to like for each account (LIKES_PER_PROFILE)
```sh
#
PROFILES_PER_TAG = 6
LIKES_PER_PROFILE = 4
```

4. Set the parameters for how long the bot will delay before proceeding to the next hashtag (in minutes). Delays are integrated to stall the bot to prevent it from liking too many pictures in quick secession and get flagged by Instagram.
```sh
delay_time = 35 
delay_variance = 15
```
Here delay_time is set to 35 minutes and the variance is 15 minutes. So, the bot will pause for between 20 to 50 minutes (35 +/- 15)

5. Set various rules for if and how you would like to engage with certain accounts, such as would you like to comment on an account that is already following you (COMMENT_IF_FOLLOWING)
```sh
COMMENT_IF_FOLLOWING = False
LIKE_IF_FOLLOWING = True
INTERACT_IF_FOLLOW_BACK = False #False means thats if an account is following you but you are not following them, you will skip it
COMMENT_ON_VIDEOS = True
LIKE_VIDEOS = True
COMMENT_ON_PICS = True
LIKE_PICS = True 
```

6. If you wish, you can set a limit on the follower to following ratio an account has. 
 * Example: if an account has 400 followers and is following 100 people, they have a ratio of 4. If configured to 3, you will skip accounts with ratios above 3
```sh
FOLLOWER_TO_FOLLOWING_RATIO_LIMIT = 3
```

7. Enter the canned comments you would like to leave on pictures. You have an option for how you would like to generate these commments.
	
	A. Use set comments that the bot will select from:
 	* To do this just have one array of comments and the bot will select one of them randomly from the list
	
	B. Use options for each part of comments that the bot will combine randomly to generate the comments:
 	* To do this have multiple arrays will different parts that will be combined to create unique comments for each post (see example below)
 ```sh
 WORD_OPTIONS = [['Wow, ','So ','Absolutely ',"Holy fluff. You're ", 'Awwww ', "By our fluffy paws! You're ", 'Absocutely '],
               ['so cute','adorable','lovely','so sweet','so so adorable','fabulous'],
               ['! ','!! ','!!! '], 
               ['❤️', '❤️🥰❤️', '❤️❤️❤️', '💕💕💕', '🔥', '🔥🔥' ,'😍', '😍😍', '😍🥰', '🥰💕']]
               
 ```
 In the above case, the bot will take one item from the first, second, third, and fourth array at random to make a comment such as "Wow so cute! 💕💕💕" or "Awwww so so adorable!! 😍"
 
8. The bot will search the captions of the pictures you are engaging to ensure the content is appropriate. You can set the bad words parameter such that if the bot finds these in the post, it will skip it. This is to prevent against, for instance, commenting "Holy fluff you're fabulous!" on a sad or grieving post.
```sh
BAD_WORDS = ['surgery','dead','rip','sad','death','tears','worst',
			 'pain','danger','terrible','awful','memory','peace']
```

9. Finally, set the list of hashtags you would like to run through. The bot will pick one at random and will not visit the same hashtag twice in the same session. 
```sh
HASHTAG_LIST = ['dachshund', 'dachshunds', 'dachshundsonly', 'dachshund_love',
                'doxiesofig', 'doxiefever']
```
<!-- USAGE EXAMPLES -->
## Usage

Following the set up by updating and personalizing the configuration settings, you can run the bot from the command line.
1. Navigate to the instabot directory
2. Run the following command:
```sh
python3 instabot.py
```
The program will open a chrome or firefox browser and navigate to instagram.com. Once there, it will input the account credentials.

3. The program will present a prompt for options. Select R and press ENTER to run the bot. It will log the activity in the terminal.
```sh
L - like pictures
R - Run the Bot
X - exit app
What would you like to do:
```
4. Sit back and relax

### Bot Data
---------------------
The bot will save the data of the users it engages and log the stats of your followers and following counts as well as the data for each run of the bot (profiles engaged, comments posted, pictures liked, and total time elapsed). This data is stored locally in a sqlite file. The path and name of the file are configurable in the config.py file.

An easy way to view the contents of the sqlite file, if you are not familiar, is to upload it to the site below:
http://sqliteviewer.flowsoft7.com/

￼

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Jake Robinson (jakerobinson19@gmail.com)

Project Link: [https://github.com/jakerobinson19/instabot](https://github.com/jakerobinson19/instabot)




