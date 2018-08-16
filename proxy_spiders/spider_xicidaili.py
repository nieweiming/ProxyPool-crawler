from bs4 import BeautifulSoup
import threading

from logic import logic_common
from logger.error_log import error_log
from logger.info_log import info_log


def crawl():
    urls = ['http://www.xicidaili.com/nn/', 'http://www.xicidaili.com/nn/2', 'http://www.xicidaili.com/wn/']
    result = []
    for url in urls:
        try:
            req = logic_common.build_request(url)
            table = BeautifulSoup(req.text, 'lxml').find('table', id='ip_list').find_all('tr')
        except Exception as e:
            error_log.error('Spider xicidaili error.[msg]={}'.format(e))
            continue
        for tr in table[1:]:
            try:
                tds = tr.find_all('td')
                ip = tds[1].get_text() + ':' + tds[2].get_text()
                result.append(ip)
            except:
                pass
    info_log.info('Spider xicidaili success.Crawled IP Count:{}'.format(len(result)))
    return result


class SpiderXicidaili(threading.Thread):
    def __init__(self):
        super(SpiderXicidaili, self).__init__()
        self.daemon = True

    def run(self):
        self.result = crawl()
