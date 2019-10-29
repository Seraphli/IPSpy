def get_ip_detail():
    import requests
    from bs4 import BeautifulSoup
    import socket
    """Get public IP and country"""
    url = r'https://www.whatismyip.org/my-ip-address'
    session = requests.Session()
    session.trust_env = False
    r = session.get(url)
    parsed_html = BeautifulSoup(r.text, 'html.parser')
    table = parsed_html.find_all('table')[0]
    label = [i.text for i in table.find_all('strong')]
    content = [i.text for i in table.find_all('span')]
    detail = dict(zip(label, content))
    ip = detail['Your IP']
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
