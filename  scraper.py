import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    contents = soup.find_all('p')
    counter = 0
    for p_content in contents:
        s_content = p_content.find_all('span')
        if s_content:
            counter += 1
    return str(counter) + " the count of them"


def get_citations_needed_report(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    contents = soup.find_all('p')
    new_contents = ''
    s_content = ''
    counter = 0
    for p_content in contents:
        s_content = p_content.find_all('span')
        if s_content:
            counter += 1
            new_contents += p_content.contents[0].strip() + '\n'
    # if len(s_content) > 1:
    return new_contents


if __name__ == '__main__':
    print(get_citations_needed_report(url))
    print(get_citations_needed_count(url))
