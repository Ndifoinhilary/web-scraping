from urllib.request import urlopen
from  link_finder import LinkFinder
from demo import *
from domain import *

def create_project_dir(project_name):
    pass


def creaet_data_file(project_name, base_url):
    pass


def file_to_set(crawled_file):
    pass


def set_to_file(queue, queue_file):
    pass


class Spider:

    project_name = ' '
    base_url = ' '
    demain_name = ' '
    queue_file = ' '
    crawled_file = ' '
    queue = set()
    crawled = set()

    def __init__(self,project_name , base_url , domain_name):
        Spider.project_name =project_name
        Spider.base_url = base_url
        Spider.demain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crewled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        creaet_data_file(Spider.project_name,Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    @staticmethod
    def crawl_page(thread_name , page_url):
        if page_url not in Spider.crawled:
            print(thread_name + 'Now crawling' + page_url)
            print('Queue' + str(len(Spider.queue))  + ' | Crawled ' +str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_file()
    @staticmethod
    def gather_link(page_url):
         html_string = ' '
         try:
             response = urlopen(page_url)
             if 'text/html' in response.gatheader('Content-Type'):
                 html_bytes = response.read()
                 html_string = html_bytes.decode("utf-g")
                 finder = LinkFinder(Spider.base_url,page_url)
                 finder.feed(html_string)
         except Exception as e:
             print(str(e))
             return set()
         return finder.page_links()
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.demain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)