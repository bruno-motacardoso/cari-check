from utils import badUsage
from selenium import webdriver
import datetime
import locale
import sys
import cari
import requests
import config
import os

dirname = os.path.dirname(__file__)

if(config.cari_url is None or config.wirepusher_url is None):
  print('Error: The setting is required.')
  sys.exit(1)


# args validation
noReg = None
endDate = None
fromDate = None
endDate = None
try:
  noReg = sys.argv[1]
except IndexError:
  badUsage(sys.argv[0])

try:
  dateOfBirth = datetime.datetime.strptime(sys.argv[2], '%d.%m.%Y')
except IndexError:
  badUsage(sys.argv[0])

try:
  fromDate = datetime.datetime.strptime(sys.argv[3], '%d.%m.%Y')
except IndexError:
  badUsage(sys.argv[0])

try:
  endDate = (datetime.datetime.strptime(sys.argv[4], '%d.%m.%Y')).replace(hour=23, minute=59)
except IndexError:
  badUsage(sys.argv[0])

try:
  wirepusher_id = sys.argv[5]
except IndexError:
  badUsage(sys.argv[0])

print('Script options successfully loaded.')
print('\tnoReg = %s' % noReg)
print('\tdateOfBirth = %s' % dateOfBirth)
print('\tfromDate = %s' % fromDate)
print('\tendDate = %s' % endDate)
print('\twirepusher_id = %s' % wirepusher_id)

# sys.exit()

locale.setlocale(locale.LC_ALL, 'fr_CH')
driver_filename = os.path.join(dirname, 'chromedriver.exe')
driver = webdriver.Chrome(driver_filename)

cari.login(driver=driver, noReg=noReg, dateOfBirth=dateOfBirth)

cari.changeDate(driver=driver)

availability = cari.serachAvailability(driver=driver)
while availability is None:
  cari.nextWeek(driver=driver)
  availability = cari.serachAvailability(driver=driver)

driver.close()
avaStr = 'Availability found for ' + availability.strftime('%d.%m.%Y %H:%M') + '. Run and book the date!'
print(avaStr)

if availability > fromDate and availability < endDate:
  print('An availability was found on desired a date.')
  r = requests.post('https://wirepusher.com/send', data={'id': wirepusher_id, 'title': 'Cari-check: Trouvé', 'message': avaStr, 'type': 'Important', 'action': config.cari_url})
  if r.status_code == 200:
    print('Notification sent.')
  else:
    print('Error when sending notification.')
else:
  print(f'No availability found on desired dates (from {fromDate} to {endDate}).')
  # r = requests.post('https://wirepusher.com/send', data={'id': wirepusher_id, 'title': 'Cari-check: Pas trouvée', 'message': avaStr, 'action': config.cari_url})
  # print(r)
  # if r.status_code == 200:
  #   print('Notif envoyée')

sys.exit(0)