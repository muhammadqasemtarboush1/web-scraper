import requests
from bs4 import BeautifulSoup


# Create function named get_citations_needed_count
# takes in a url string and returns an integer.


# Create function named get_citations_needed_report
# takes in a url string and returns a report string
# the string should be formatted with each citation listed in the order found.



url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
r = requests.get(url)

soup = BeautifulSoup(r.content , 'html.parser')

jobs_cards = soup.find_all('p','sub')

all_jobs = []

for job in jobs_cards:
    job
    print(job,"ededede")


job_titles = soup.find_all('h2', class_ = 'jb-title')
print(job_titles)