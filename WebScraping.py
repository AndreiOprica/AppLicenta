from bs4 import BeautifulSoup
import requests
import re
import sqlite3

links_patterns = re.compile(r'/servlet/event.showcfp?\S*')
remove_tags_pattern = re.compile(r'<[^>]+>')


def find_links(text):
    return re.findall(links_patterns, text)


def remove_tags(text):
    return remove_tags_pattern.sub('', text)


def scrap_pages_links(uri):
    req = requests.get(uri)
    soup = BeautifulSoup(req.text, 'html.parser')
    find = soup.findAll('a')
    text = find_links(str(find))
    for e in range(len(text)):
        one_string = str(text[e])
        formated = one_string.split('"')
        text[e] = 'http://www.wikicfp.com/cfp' + formated[0]
    return text


def scrap_page(uri):

    req = requests.get(uri)
    soup = BeautifulSoup(req.text, 'html.parser')
    text = soup.findAll('div', {"class": "contsec"})
    text_without_tags = remove_tags(str(text))
    edited_data = text_without_tags.split("\n")
    edited_data = [element for element in edited_data if element]
    for element in range(len(edited_data)):
        edited_data[element] = edited_data[element].strip()

    no = -1
    for element in range(len(edited_data)):
        if edited_data[element] == 'Related Resources':
            no = element - 1
            break

    if no != -1:
        del edited_data[no:len(edited_data)]

    del edited_data[0:3]
    return edited_data



urls = [
    # linkuri spre categoria de computer science
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=1',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=2',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=3',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=4',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=5',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=6',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=7',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=8',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=9',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=10',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=11',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=12',
#    'http://www.wikicfp.com/cfp/call?conference=computer%20science&page=13',

    # linkuri spre categoria de machine learning
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=1',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=2',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=3',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=4',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=5',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=6',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=7',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=8',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=9',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=10',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=11',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=12',
#    'http://www.wikicfp.com/cfp/call?conference=machine%20learning&page=13',
]

data = []
for url in urls:
    links_from_url = scrap_pages_links(url)
    for el in links_from_url:
        element = []
        scraped_data = scrap_page(el)
        for ele in scraped_data:
            if ele != '':
                element.append(ele)
        rows = 20 - len(element)
        for ele in range(rows):
            element.append(' ')
        data.append(element)


# conectare cu baza de date si introducerea inregistrariilor
conn = sqlite3.connect('identifier.sqlite')
c = conn.cursor()
c.executemany('INSERT INTO datas VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);', data)
conn.commit()
conn.close()

