# Intro
This tool is used to check the availabilities to pass the car exam at Geneva. It was developed because the waiting time to the next exam session is too long (sometimes 6 months).
The hack works like following:
1. Book the exam for the next available date => https://ge.ch/cari-online/examensPublic
2. Schedule this tool (e.g. every hour) and it will find an availability on an desired date (see params).
3. When a schedule is found, you will receive a notification on your smartphone (wirepusher).
4. Book manually the exam on desired date

# Requirements
Install wirepusher on your smartphone to receive notifications.
http://wirepusher.com/

Install requirements for the python script:

```
pip install -U selenium
python -m pip install requests
```

I use the following versions of chrome and chromedriver:
- Chrome version 91
- Chrome Driver version 91

# Improvements to do
- Be able to send notifications on ios, it seems that wirepusher is not available on ios.
- Dockerize? the application to can be scheduled on a cloud. Like a serveless app with lower costs.