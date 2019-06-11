import requests
import socket
import json


def get_ip_detail():
    """Get public IP and country"""
    url = r'http://www.trackip.net/ip?json'
    r = requests.get(url)
    detail = json.loads(r.text)
    ip = detail['IP']
    country = detail['Country']
    hostname = socket.gethostname()
    return ip, country, hostname


if __name__ == '__main__':
    print(get_ip_detail())
