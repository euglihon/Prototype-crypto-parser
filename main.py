import requests
from bs4 import BeautifulSoup
import csv

# https://coinmarketcap.com/

def write_csv(data):
    with open('coins.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow( [data['name'], data['price'], data['url'] ] )


def re_find(string):
    '''
    $8,705.75 => 8,705.75
    '''
    result = string.replace('$', '')
    return result


def get_html(url):
    responses = requests.get(url)
    html = responses.text
    return html


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    rows_coins = soup.find('tbody').find_all('tr')

    for row in rows_coins:
        td = row.find_all('td')

        name_coins = td[1].text
        url_coins = 'https://coinmarketcap.com' + td[1].find('a').get('href')
        price_coins = td[3].text
        final_price_coins = re_find(price_coins)

        data = {
            'name': name_coins,
            'price': final_price_coins,
            'url': url_coins
        }

        write_csv(data)


def main():
    url = 'https://coinmarketcap.com'
    get_data(get_html(url))


if __name__ == '__main__':
    main()