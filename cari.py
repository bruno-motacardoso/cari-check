from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import datetime
import config


def login(driver, noReg, dateOfBirth):
  driver.get(config.cari_url)

  noRegInput = driver.find_element_by_name('noReg')
  noRegInput.send_keys(noReg)

  dateJJInput = driver.find_element_by_name('dateJJ')
  dateJJInput.send_keys(dateOfBirth.day)

  dateMMInput = driver.find_element_by_name('dateMM')
  dateMMInput.send_keys(dateOfBirth.month)

  dateAAAAInput = driver.find_element_by_name('dateAAAA')
  dateAAAAInput.send_keys(dateOfBirth.year)

  validerButton = driver.find_element_by_name('valider')
  validerButton.send_keys(Keys.RETURN)

def nextWeek(driver):
  nextWeek = driver.find_element_by_name('nextWeek')
  nextWeek.send_keys(Keys.RETURN)


def serachAvailability(driver):
  table = driver.find_element_by_id('idDivTablePlaceLibre').find_element_by_tag_name('table')
  trs = table.find_elements_by_tag_name('tr')
  header = trs[0] # header contenant les jours
  body = trs[1] # body contenant les plages horaires

  headerTds = header.find_elements_by_tag_name('td')
  bodyTds = body.find_elements_by_tag_name('td')
  i = 0
  while i < len(bodyTds):
    try:
      hour = bodyTds[i].find_element_by_tag_name('a').text
      if(i%2 == 0):
        z=int(i/2)
      else:
        z=int((i+1)/2)
      
      day = (headerTds[z].find_element_by_tag_name('font').text).split(': ')[1]
      availibilityDatetime = datetime.datetime.strptime(day + ' ' + hour, '%d.%m.%Y %H:%M')
      return availibilityDatetime
    except NoSuchElementException:
      pass
    i+=1
  return None
    
