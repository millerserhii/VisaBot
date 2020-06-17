import requests
from bs4 import BeautifulSoup
import re
import json


URL = 'https://mfa.gov.ua/podorozhnim/krayini-svitu-poperedzhennya-ta-poradi-rezhim-vyizdu'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'
,
    'accept':'*/*',
    'content-type':	'text/html; charset=UTF-8'
}

def get_html(url, headers=HEADERS, params=None):
    r = requests.get(url, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items =  soup.find_all(class_='card accordion_sidebar__card accordion_static__card')
    countries = {}

    for item in items:
        countries.update({
            item.find('button', class_='btn accordion_sidebar__btn accordion_static__btn collapsed').get_text():
            item.find(class_='card-body editor-content accordion_static__body').get_text()


        })
    data = {re.sub('\n\t\t\t\t', '', key): re.sub('\xa0', '', value) for key, value in countries.items()}
    data = {re.sub('\t', '', key): re.sub('\n', '', value) for key, value in data.items()}
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()

