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
json: 

'def creating_suitable_prices():
    session = requests.Session()
    request = session.get('https://spreadsheets.google.com/feeds/list' +
                          '/1Lscd6K7wVHbD5kUHBhXnecxCayknR8sIFy-dtS2Wny4/od6/public/values?alt=json',
                          headers=NewGames.HEADERS)
    table_json = request.json()
    table_len = len(table_json['feed']['entry'])
    titles = [table_json['feed']['entry'][title]['gsx$games']['$t'] for title in range(table_len)]
    prices = [int(table_json['feed']['entry'][price]['gsx$prices']['$t']) for price in range(table_len)]
    suitable_prices = {title: price for title, price in zip(titles, prices)}
    return suitable_prices'

If the price of the new offer corresponds to the price indicated in the Google
sheet, then the bot will send a notification in the form of a telegram message.
 
 
