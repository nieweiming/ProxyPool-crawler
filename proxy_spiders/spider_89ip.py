import re
import time
import threading

from logic import logic_common
from logger.error_log import error_log
from logger.info_log import info_log


def crawl():
    urls = ['http://www.89ip.cn/tiqv.php?sxb=&tqsl=300&ports=&ktip=&xl=on&submit=%CC%E1++%C8%A1']
    result = []
    for pageurl in urls:
        try:
            req = logic_common.build_request(pageurl)
            html = req.text
        except Exception as e:
            error_log.error('Spider 89ip error.[msg]={}'.format(e))
            continue
        ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', html)
        result += ips
        time.sleep(2)
    info_log.info('Spider 89ip success.Crawled IP Count:{}'.format(len(result)))
    return result


class SpiderIP89(threading.Thread):
    def __init__(self):
        super(SpiderIP89, self).__init__()
        self.daemon = True


    def run(self):
        self.result = crawl()
