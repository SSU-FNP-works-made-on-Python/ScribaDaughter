import requests
from bs4 import BeautifulSoup
import json


def parse_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "lxml")


def load_department(department):
    url = f'https://scribabot.tk/api/v1.0/group/number/{department}/do/4'
    soup = parse_page(url)
    numberofgroup = soup.find('p').contents[0]
    numgroup = json.loads(numberofgroup)['groupNumbers']
    if not numgroup:
        numgroup = ["группы не найдены"]
    return numgroup


if __name__ == '__main__':
    load_department(department = 'nbmt')