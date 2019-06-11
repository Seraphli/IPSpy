import requests
import json


def get_ip_detail():
    """Get public IP and country"""
    url = r'http://www.trackip.net/ip?json'
    r = requests.get(url)
    detail = json.loads(r.text)
    country = detail['Country']
    ip = detail['IP']
    return country, ip


if __name__ == '__main__':
    print(get_ip_detail())
