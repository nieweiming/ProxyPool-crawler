import threading
from bs4 import BeautifulSoup

from logic import logic_common
from logger.error_log import error_log
from logger.info_log import info_log


def crawl():
    urls = ['http://www.data5u.com/free/gngn/index.shtml', 'http://www.data5u.com/free/gwgn/index.shtml',
            'http://www.data5u.com/free/gnpt/index.shtml', 'http://www.data5u.com/free/gwpt/index.shtml']
    result = []
    for url in urls:
        try:
            req = logic_common.build_request(url)
            table = BeautifulSoup(req.text, 'lxml').find_all('ul', {"class": 'l2'})
        except Exception as e:
            error_log.error('Spider data5u error.[msg]={}'.format(e))
            continue
        for item in table[1:]:
            try:
                spans = item.find_all('span')
                ip = spans[0].get_text()
                port = spans[1].get_text()
            except:
                continue
            line = ip + ':' + port
            result.append(line.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', ''))
    info_log.info('Spider data5u success.Crawled IP Count:{}'.format(len(result)))
    return result


class SpiderData5u(threading.Thread):
    def __init__(self):
        super(SpiderData5u, self).__init__()
        self.daemon = True


    def run(self):
        self.result = crawl()
