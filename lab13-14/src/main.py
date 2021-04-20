import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import http.client
import time
import json


def rem(str1):
    s = str1.replace('</span>', '')
    s = s.replace('<span>', '')
    s = s.replace('</b>', '')
    s = s.replace('<b>', '')
    s = s.replace('<p>', '')
    s = s.replace('</p>', '')
    s = s.replace('</div>', '')
    return s


# key = 'd9efbb6d-76a1-4c65-bbfa-6b3240ac739d'
def main():
    host = 'ua.jooble.org'


    key = '652999ab-b164-4993-a771-089a9b56e8a3'

    connection = http.client.HTTPConnection(host)
    # request headers
    headers = {"Content-type": "application/json"}
    # json query
    body = '{ "keywords": "Senior Python", "location": "Kyiv", "salary": "120000"}'
    connection.request('POST', '/api/' + key, body, headers)
    response = connection.getresponse()
    print(response.status, response.reason)
    data = response.read().decode('UTF-8')
    data = data.replace(':', ': ')
    data = data.replace(',', ', ')
    data = data.replace('<b>', ', ')
    data = data.replace('</b>', ', ')
    data = data[28:-2]
    a = eval(data)
    for i in range(0, len(a)):
        if 'company' in a[i]:
            print(f'Job №{i+1}\n')
            print(a[i]['title'] + ' ' + a[i]['salary'] + ' ' + a[i]['snippet'] + ' ' + a[i]['company'] + ' ' +
                  a[i]['location'])
        else:
            print(f'Job №{i+1}\n')
            print(a[i]['title'] + ' ' + a[i]['salary'] + ' ' + a[i]['snippet'] + ' ' + a[i]['location'])
    print('\n\n')


    salary = 16000
    url = f'https://ua.jooble.org/SearchResult?salaryMin={salary}&ukw=data%20scientist'
    r = requests.get(url)
    result = pd.DataFrame()
    soup = BeautifulSoup(r.text, 'html.parser')  # Отправляем полученную страницу в библиотеку для парсинга
    title = soup.find_all("span", {'class': 'a7df9'})
    salary = soup.find_all("p", {'class': '_0010f'})
    company = soup.find_all("p", {'class': '_786d5'})
    location = soup.find_all("div", {'class': 'caption _7076d'})
    f = list()
    for i in range(0, len(title)):
        title = soup.find_all("span", {'class': 'a7df9'})
        title = rem(str(title[i]))
        title = title.replace('<span class="a7df9">', '')
        if i < len(salary):
            salary = soup.find_all("p", {'class': '_0010f'})
            salary = rem(str(salary[i]))
            salary = salary.replace('<p class="_0010f">', '')
        else: salary = ''
        company = soup.find_all("p", {'class': '_786d5'})
        company = rem(str(company[i]))
        company = company.replace('<p class="_786d5">', '')
        location = soup.find_all("div", {'class': 'caption _7076d'})
        location = rem(str(location[i]))
        location = location.replace('<div class="caption _7076d">', '')
        n = [title, salary, company, location]
        f.append(list(n))

    # data = pd.DataFrame(d)
    # for i in range(0, len(response)):
    #     print(response.read()[i])
    # data.to_csv('pars.csv')

    with open('pars.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(f)

    with open('pars.csv', "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(300)
