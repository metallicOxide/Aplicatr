from bs4 import BeautifulSoup
import os
from requests_html import HTMLSession
import sys
from typing import List, Dict, Any
from pprint import pprint

username = os.environ['UNSW_USERNAME']
password = os.environ['UNSW_PASSWORD']

def login() -> (HTMLSession):
    print("Creating session...")
    sesh = HTMLSession()

    print("Extracting login page tokens...")
    loginPage = sesh.get('https://careersonline.unsw.edu.au/students/login')
    soup = BeautifulSoup(loginPage.content, "html.parser")
    requestVerificationToken = soup.find("input", {'name': '__RequestVerificationToken'}).get('value')
    loginPayload = {
        'LDAPUsername': username, 
        'LDAPPassword': password,
        '__RequestVerificationToken': requestVerificationToken
    }
    
    print("Logging in to the UNSW careers online portal...")
    setCookies = sesh.post('https://careersonline.unsw.edu.au/providers/ldap/Login/1', data=loginPayload)
    if not setCookies.ok: 
        print("Error setting cookies, exiting...")
        sys.exit()
    login = sesh.post('https://careersonline.unsw.edu.au/')
    if not login.ok: 
        print("Error logging in, exiting...")
        sys.exit()
    print("Logged into UNSW careers online portal!")
    
    return sesh

def extractData(sesh: HTMLSession) -> List[Dict]:
    print("Extracting all job listings...")
    jobBoard = sesh.get('https://careersonline.unsw.edu.au/students/jobs/Search?text=&typeofwork=-1&location=&page=1&take=1000')
    jobSoup = BeautifulSoup(jobBoard.content, features='html.parser')
    
    jobs = [{
                'title': listing.find('a').get_text().replace('\\r\\n', '').strip(),
                'link': listing.find('a')['href'],
                'summary': listing.find('p', {'class': 'job-list-summary'}).get_text(strip=True),
                'closing_date': listing.find('div', {'class': 'job-list-close'}).get_text(strip=True).replace('Closes- ', ''),
                'location': listing.find('div', {'class': 'job-list-location'}).get_text(strip=True)
            } 
            for listing in jobSoup.find_all("div", {"class": 'list-group-item'})]
    pprint(jobs)
    return jobs
        
sesh = login()
extractData(sesh)
    