import socket


def get_ip_address(url):
    results = socket.gethostbyname(url)
    return results
#returns IP address


