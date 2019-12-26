# Playgame teleram bot.

**Requirements:**
  - beautifulsoup4==4.8.1
  - bs4==0.0.1
  - certifi==2019.11.28
  - chardet==3.0.4
  - idna==2.8
  - pyTelegramBotAPI==3.6.6
  - python-crontab==2.4.0
  - python-dateutil==2.8.1
  - requests==2.22.0
  - schedule==0.6.0
  - six==1.13.0
  - soupsieve==1.9.5
  - urllib3==1.25.7

# DETAILS:

  The bot using the schedule module runs every three minutes. In the course of work, he
collects information about new offers on the site (name, seller and price). The bot
compares the learned data with the data downloaded from Google sheets in the form of
json.

  Function *creating_suitable_prices()* parses google sheet and returns dict consisting
  of game names and prices:
  
    '{title: price for title, price in zip(titles, prices)}'
    
  If the price of the new offer corresponds to the price indicated in the Google
sheet, then function *check_the_entry(game)* sends a signal to the bot, after that programm
will send a notification in the form of a telegram message.
 
 
