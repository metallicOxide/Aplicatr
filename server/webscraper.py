from requests import Session
from bs4 import BeautifulSoup
import os

username = ''
password = ''

# Logging into the dashboard
def login():
    with Session() as sesh:
        loginPage = sesh.get('https://careersonline.unsw.edu.au/students/login')

        soup = BeautifulSoup(loginPage.content, "html.parser")
        requestVerificationToken = soup.find("input", {'name': '__RequestVerificationToken'}).get('value')
        
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

login()