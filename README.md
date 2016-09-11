# TakeCareOfMyPlant_BOT

### About
This code it's a bot to everyday water the plant from the subbreddit /r/takecareofmyplant.

They are used two API's to take quotes and the code will search for words like 'yes' and 'no' to give a valid comment. the system that the code follows it's the 2-1. In the future will be implemented the two systems that users are using. (3-1 and 2-1)

### Installation

One API need UID to take quotes. But you can take one from [STANDS4]. The other you can use freely.

The code requires a Raspberry Pi, Python and xml.etree.ElementTree.

Download the code.
```sh
$ mkdir JeffPlant
$ git clone https://github.com/adrianobrum/takecareofmyplant_bot.git
$ cd JeffPlant
$ mkdir logs
```

Edit the config file.
```sh
$ cd JeffPlant
$ sudo nano config.py
```

Make a cron job to run the code, one, two, three, etc... The code will just vote one time a day. But sometimes the code stop working, so make the code work every 2 hours.
```sh
$ crontab -e
```
Write in the bottom the following line.
```sh
0 */2 * * * cd /home/pi/JeffPlant && sudo python /home/pi/JeffPlant/startwater.py
```



[STANDS4]: <http://www.quotes.net/api.php>