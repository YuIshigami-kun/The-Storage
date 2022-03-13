# The Storage
The Storage is a tool made in python 3 to scrappe different types of data from telegram messages (udemy links, mega links, files...).

## Instalation

### Linux
1. >git clone https://github.com/YuIshigami-kun/The-Storage.git
2. >cd The-Storage
3. >python3 -m pip install -r requirements.txt

### Windows | Mac
1. Download the zip file
2. Uncompress the zip file and enter at the resulted directory
3. >python3 -m pip install -r requirements.txt


## Configuration
For getting the telegram api id and the telegram api hash you should follow [this guide](https://core.telegram.org/api/obtaining_api_id).

In the config.json file you have several options (all are disabled by default):

    "tg-api-id" :  0,
    "tg-api-hash" : "x",
    "version" : "0.1.0",
    "targets" : {
        "credit-cards" : false,
        "custom-text" : {
            "enabled" : false,
            "match" : "Hi!"
        },
        "proxies" : false,
        "open-bullet-configs" : false,
        "bins" : false,
        "mega-links" : false,
        "udemy-discount-courses" : false,
        "udemy-courses" : false,
        "google-drive-links" : false,
        "mediafire-links" : false,
        "anonfiles-links" : false,
        "pastebin-links" : false,
        "images" : false,
        "audios" : false,
        "code-files" : false,
        "pdf" : false,
        "custom-extension" : "",
        "files" : false,
        "videos" : false,
        "url-shorters" : false,
        "spam" : false
    },
    "save" : {
        "enabled" : false,
        "place" : "me"
    },
    "download" : false,
    "dont-scrape-from" : []

To enable most of the options **you just have to change the false to true**.

### Scrapping messages options:
|Option|Target|
| ----------- | ----------- |
|credit-cards|Valid credit cards from the most used brands|
|custom-text|Messages containing the input text|
|proxies|Proxies in the ip:port format (Support username and password)|
|open-bullet-configs|Valid files for open bullet|
|bins|First six digits from a credit card (Used un bining and data analisys)|
|mega-links|Mega links with files or folders|
|udemy-discount-courses|Udemy links with a discount coupon|
|udemy-courses|Udemy links without a discount coupon|
|google-drive-links|Google drive links with files or folders|
|mediafire-links|Same as before|
|anonfiles-links|Links from all anonfiles domains|
|pastebin-links|Links from all pastebin domains|
|images|Images compresed by telegram **no files with image extension**|
|audios|Audio or music files compresed by telegram **no files with audio extension**|
|code-files|Usual coding files like 'index.py' or 'index.php'|
|pdf|PDF extension files|
|custom-extension|All the files with the written extension (Ex. '.txt')|
|files|Non compresed files uploaded at telegram|
|videos|Compresed videos **no files with video extension**|
|url-shorters|Most common used url shorters (You can add yours in validate.py)|
|spam|Messages with spam keywords (You can add yours at index.py and this can be usefull at administration)|

### Saving options
|Option|Save place|
| ----------- | ----------- |
|save|When is enabled it saves the messages in the target input ("me" for saved messages or an id for a group\channel\chat **at an integrer format**)|
|download|Downloads the match media\messages in the Downloads folder (In diferent directories like 'images', 'videos', 'Mega.txt'...)|

### Extras
|Option|Save place|
| ----------- | ----------- |
|dont-scrappe-from|Don´t process the messages matching with the ids at the list **all with string format**|

In future updates i´ll add more options like an only-scrappe-from extra

## Contact
[Telegram](http://t.me/Yulshigami)

## Donations
BTC --> bc1q4g6h98z72dr65qnyuw44979jelk077mmc3xucl

ETH --> 0x30fd7278c10Ea6B82982a4f2717fB6dC6C238886

LTC --> LV5Y591opDFw5zBto7zCWGgxHiF66SyvbW

DOGE --> DQbK8DSG8JNmLpz7hjToHwTnpNwzXiXehn
