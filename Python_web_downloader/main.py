from general import *
from domain_name import *
from IP_address import *
from robots_txt import *


root_dir = 'companies'
create_dir(root_dir)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    robots_txt = get_robots_txt(url)
    create_file(name, url, domain_name, robots_txt)


def create_file(name, full_url, domain_name, robots_txt):
    project_dir= root_dir + '/' + name
    create_dir(project_dir)
    write_file(project_dir + 'domain_name.txt', domain_name)
    write_file(project_dir + 'robots_txt.txt', robots_txt)
    write_file(project_dir + 'full_url.txt', full_url)


site_name = str(input("Enter the site Name: "))
site_url = str(input("Enter site url: "))

gather_info(site_name, site_url)
