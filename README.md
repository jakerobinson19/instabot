<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#simple-instagram-bot)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## Simple Instagram Bot
-----------------------
There are several instagram bots available on Github, this one is tailored to the goal of follower growth by applying Gary Vaynerchuks $1.80 strategy of commenting on approximately 90 unique accounts everyday. This bot takes the strategy one step further by also liking several of the past photos for accounts that are commented on. However, while a key part of the $1.80 strategy is using comments related to the pictures content, this automated bot can only allow limited customization of comments.

The user will be able to specify the rules of engagement including how many accounts to view, how many pictures of each account to like or comment on, and if and what to comment on pictures.

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python 3.7](https://www.python.org/downloads/)
* [Selenium](http://www.seleniumhq.org/download/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- This code was written using [Python 3.7](https://www.python.org/downloads/).
- [Selenium](http://www.seleniumhq.org/download/) (this can be PIP installed, written using v3.0.2).
- The Selenium package requires a webdriver program. This code was written 
using [Chromedriver](https://chromedriver.storage.googleapis.com/index.html) v78.

```sh
pip install requirements.txt
```

### Installation
#### Windows:
pip install selenium

#### MacOS:
```sh
sudo easy_install selenium
```
### Install drivers:

Selenium requires a web driver to access the latest and greatest features. For the bot to work, you should download the webdriver for the browser that you plan to use and, once downloaded, add the driver to your $PATH by putting it in your */usr/local/bin* or */usr/bin* directories (depending on where Python is installed). 

For a full list of drivers to download for Selenium, go to: https://www.seleniumhq.org/download/

Otherwise, here are links to the most popular drivers.

| Browser        | Link                                                        |
|---|---|
| Chrome         | https://sites.google.com/a/chromium.org/chromedriver/       |
| Firefox        | https://github.com/mozilla/geckodriver/                     |

Note: to see the version of the browser you have go to Settings>About Chrome or Menu>Help>About FireFox

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_


### Bot Data
---------------------
The bot will save the data of the users it engages and log the stats of your followers and following counts as well as the data for each run of the bot (profiles engaged, comments posted, pictures liked, and total time elapsed). This data is stored locally in a sqlite file. The path and name of the file are configurable in the config.py file.

An easy way to view the contents of the sqlite file, if you are not familiar, is to upload it to the site below:
http://sqliteviewer.flowsoft7.com/





