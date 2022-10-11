import requests
from bs4 import BeautifulSoup as bs
import os.path


def find_length(lecture):
    length_start = str(lecture).find('Length') + 7
    length_end = str(lecture).find(' ', length_start)
    try:
        length = int(str(lecture)[int(length_start):int(length_end)])
        return length
    except ValueError:
        return 0


def update_file(fname, f2): #возвращает 1 когда был такой же файл, 2 когда файлы были разные, 0 когда файла не было
    return_value = 1
    flag = 0
    if not os.path.exists(fname):
        with open(fname, 'wb') as f:
            f.write(f2)
        return 0

    with open(fname, 'rb') as f:
        if find_length(f2) != find_length(f.read()):
            flag = 1
    if flag == 1:
        with open(fname, 'wb') as f:
            f.write(f2)
        return 2
    return 1


def parseMatan():
    url = "https://math.hse.ru/"
    r = requests.get('https://math.hse.ru/mathan1_medved_fall22')
    soup = bs(r.content, "html.parser")
    htmlfiles = soup.find_all('a', class_='link mceDataFile', href=True)
    names = dict()
    for x in htmlfiles:
        names[x.text + '.pdf'] = update_file('Matan\\' + x.text + ".pdf", requests.get(url + x['href']).content)

    return names

def parseGeom():
    # url = "https://math.hse.ru/"
    r = requests.get('http://me.hse.ru/avilov/материалы-курса-геометрия/')
    soup = bs(r.content, "html.parser")
    htmlfiles = soup.find_all('div', class_='wp-block-file')
    names = dict()
    for file in htmlfiles:
        link = file.find('a', href = True)
        names[link.text + '.pdf'] = update_file('Geom\\' + link.text + '.pdf', requests.get(link['href']).content)

    return names


if __name__ == '__main__':
    parseGeom()