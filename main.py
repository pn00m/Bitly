import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

API_URL = "https://api-ssl.bitly.com/v4/"
bitlink_token = os.environ['BITLY_TOKEN']


def shorten_link(headers, link):
    long_url = {
        "long_url": link,
    }
    url_shorten = f"{API_URL}shorten"
    response = requests.post(url_shorten, headers=headers, json=long_url)
    bitlink = response.json()
    return bitlink['id']


def count_clicks(headers, link):
    params = {
        ('unit', 'day'),
        ('units', '-1')
    }
    url_clicks = f"{API_URL}bitlinks/{link}/clicks/summary"
    response = requests.get(url_clicks, headers=headers, params=params)
    return response.json()


def is_bitlink(headers, link):
    is_bitlink_url = f"{API_URL}bitlinks/{link}"
    response = requests.get(is_bitlink_url, headers=headers)
    return response.ok


def check_url_accessibility(link):
    response = requests.get(link)
    response.raise_for_status()
    return response.status_code


def main():
    load_dotenv()
    oauth_headers = {
        "Authorization": f"Bearer {bitlink_token}"
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('input_url', help='Ссылка для обрезки или статистики')
    args = parser.parse_args()
    input_link = args.input_url
    url_without_protocol = urlparse(input_link).netloc \
        + urlparse(input_link).path
    try:
        check_url_accessibility(input_link)
        if is_bitlink(oauth_headers, url_without_protocol):
            clicks_count = count_clicks(oauth_headers, url_without_protocol)
            print(
                'По вашей ссылке прошли:',
                clicks_count['total_clicks'], 'раз(а)'
            )
        else:
            bitlink = shorten_link(oauth_headers, input_link)
            print ('Битлинк: ', bitlink)
    except requests.exceptions.HTTPError:
        print('Ссылка не существует')
    except requests.exceptions.MissingSchema:
        print('Это не ссылка')
    except requests.exceptions.InvalidURL:
        print('Ссылка не валидна')

if __name__ == '__main__':
    main()
