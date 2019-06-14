def get_ip_detail():
    import requests
    import json
    import socket
    """Get public IP and country"""
    url = r'http://www.trackip.net/ip?json'
    r = requests.get(url)
    detail = json.loads(r.text)
    ip = detail['IP']
    country = detail['Country']
    hostname = socket.gethostname()
    return ip, country, hostname


def get_mac_addr():
    import re
    import uuid
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))


if __name__ == '__main__':
    print(get_ip_detail())
    print(get_mac_addr())
