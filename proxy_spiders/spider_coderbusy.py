import threading
from bs4 import BeautifulSoup

from logic import logic_common
from logger.error_log import error_log
from logger.info_log import info_log


def crawl():
    result = []
    for page in range(5):
        url = 'https://proxy.coderbusy.com/classical/anonymous-type/highanonymous.aspx?page=%s' % (page + 1)
        try:
            req = logic_common.build_request(url)
            table = BeautifulSoup(req.text, 'lxml').find('div', {'class': 'table-responsive'}).find_all('tr')
        except Exception as e:
            error_log.error('Spider CoderBusy error.[msg]={}'.format(e))
            continue
        for item in table[1:]:
            try:
                tds = item.find_all('td')
                ip = tds[0].get_text()
                port = tds[2].get_text()
            except:
                continue
            line = ip + ':' + port
            result.append(line.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', ''))
    info_log.info('Spider CoderBusy success.Crawled IP Count:{}'.format(len(result)))
    return result


class SpiderCoderBusy(threading.Thread):
    def __init__(self):
        super(SpiderCoderBusy, self).__init__()
        self.daemon = True

    def run(self):
        self.result = crawl()


if __name__ == '__main__':
    crawl()
