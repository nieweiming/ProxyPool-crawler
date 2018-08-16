from bs4 import BeautifulSoup
import threading

from logic import logic_common
from logger.error_log import error_log
from logger.info_log import info_log


def crawl():
    result = []
    for page in range(1, 10):
        url = 'https://www.kuaidaili.com/ops/proxylist/{}/'.format(page)
        try:
            req = logic_common.build_request(url)
            table = BeautifulSoup(req.text, 'lxml').find(
                'div', {'id': 'freelist'}).find('table').find_all('tr')
        except Exception as e:
            error_log.error('Spider kuaidaili error.[msg]={}'.format(e))
            continue
        for tr in table[1:]:
            try:
                ip = tr.find('td', {'data-title': 'IP'}).get_text()
                port = tr.find('td', {'data-title': 'PORT'}).get_text()
                ip = ip + ':' + port
                result.append(ip)
            except:
                pass
    info_log.info('Spider kuaidaili success.Crawled IP Count:{}'.format(len(result)))
    return result


class SpiderKuaidaili(threading.Thread):
    def __init__(self):
        super(SpiderKuaidaili, self).__init__()
        self.daemon = True


    def run(self):
        self.result = crawl()
