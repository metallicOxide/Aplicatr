# from requests import Session
from bs4 import BeautifulSoup
import os

from requestium import Session, Keys

from seleniumrequests import Firefox # Allows you to launch/initialise a browser.
from selenium import webdriver
from selenium.webdriver.firefox.options import Options # To make browser headless
from selenium.webdriver.common.by import By # Allows you to search for things using specific parameters.
from selenium.webdriver.support.ui import WebDriverWait # Allows you to wait for a page to load.
from selenium.webdriver.support import expected_conditions as EC # Specify what you are looking for on a specific page in order to determine that the webpage has loaded.
from selenium.common.exceptions import TimeoutException # Handling a timeout situation.

username = 'z5120423'
password = 'mBo2135879orange'

def login0():
    '''
    Logs into dashboard, but unable to parse subsequent dynamically generated content
    '''
    with Session() as sesh:
        loginPage = sesh.get('https://careersonline.unsw.edu.au/students/login')

        soup = BeautifulSoup(loginPage.content, "html.parser")
        requestVerificationToken = soup.find("input", {'name': '__RequestVerificationToken'}).get('value')
        print (requestVerificationToken)
        loginPayload = {
            'LDAPUsername': username, 
            'LDAPPassword': password,
            '__RequestVerificationToken': requestVerificationToken
        }
        
        sesh.post('https://careersonline.unsw.edu.au/providers/ldap/Login/1', data=loginPayload)
        response = sesh.post('https://careersonline.unsw.edu.au/')
        html = response.content
        soup = BeautifulSoup(html, features="html.parser")
        print(soup)


def login1():
    '''
    The library requestium feels like too many dependencies, very easily 
    broken. Right now, cookies expiry broken and not work
    '''
    
    s = Session(webdriver_path='./chromedriver', 
                   browser='chrome', 
                   default_timeout=15)
    s.driver.get('https://careersonline.unsw.edu.au/students/login')
    requestVerificationToken = s.driver.find_element_by_name(name='__RequestVerificationToken').get_attribute('value')
    loginPayload = {
        'LDAPUsername': username, 
        'LDAPPassword': password,
        '__RequestVerificationToken': requestVerificationToken
    }
    s.transfer_driver_cookies_to_session()
    s.post('https://careersonline.unsw.edu.au/providers/ldap/Login/1', data=loginPayload)
    s.post('https://careersonline.unsw.edu.au/')
    
    for cookie in s.cookies:
        s.driver.add_cookie({
            'name': cookie.name, 
            'value': cookie.value,
            'domain': cookie.domain
        }) 
    print(s.driver.page_source)     

def post(driver, path, params):
    driver.execute_script(
        '''
        let path = arguments[0];
        let params = arguments[1];
        method='post';
        // The rest of this code assumes you are not using a library.
        // It can be made less wordy if you use one.
        const form = document.createElement('form');
        form.method = method;
        form.action = path;

        for (const key in params) {
            if (params.hasOwnProperty(key)) {
            const hiddenField = document.createElement('input');
            hiddenField.type = 'hidden';
            hiddenField.name = key;
            hiddenField.value = params[key];

            form.appendChild(hiddenField);
            }
        }

        document.body.appendChild(form);
        form.submit();
        ''',
        path, params
    )
    return driver

def login2():
    ''' Ideally use selenium, but no easy straightforward way to make a post requests '''
    # https://stackoverflow.com/questions/5660956/is-there-any-way-to-start-with-a-post-request-using-selenium
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(firefox_options=options)
    browser.get('https://careersonline.unsw.edu.au/students/login')
    requestVerificationToken = browser.find_element_by_name(name='__RequestVerificationToken').get_attribute('value')
    loginPayload = {
        'LDAPUsername': username, 
        'LDAPPassword': password,
        '__RequestVerificationToken': requestVerificationToken
    }
    browser = post(browser, )

login()
    


/**
 * sends a request to the specified url from a form. this will change the window location.
 * @param {string} path the path to send the post request to
 * @param {object} params the paramiters to add to the url
 * @param {string} [method=post] the method to use on the form
 */

function post(path, params, method='post') {

  // The rest of this code assumes you are not using a library.
  // It can be made less wordy if you use one.
  const form = document.createElement('form');
  form.method = method;
  form.action = path;

  for (const key in params) {
    if (params.hasOwnProperty(key)) {
      const hiddenField = document.createElement('input');
      hiddenField.type = 'hidden';
      hiddenField.name = key;
      hiddenField.value = params[key];

      form.appendChild(hiddenField);
    }
  }

  document.body.appendChild(form);
  form.submit();
}