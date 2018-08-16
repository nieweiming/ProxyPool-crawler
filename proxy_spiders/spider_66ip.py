import re
import time
import threading

from logic import logic_common
from logger.error_log import error_log
from logger.info_log import info_log


def crawl():
    urls = [
        'http://www.66ip.cn/nmtq.php?getnum=600&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=66ip']
    result = []
    for pageurl in urls:
        try:
            req = logic_common.build_request(pageurl)
            html = req.text
        except Exception as e:
            error_log.error('Spider 66ip error.[msg]={}'.format(e))
            continue
        ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', html)
        result += ips
        time.sleep(2)
    info_log.info('Spider 66ip success.Crawled IP Count:{}'.format(len(result)))
    return result


class SpiderIP66(threading.Thread):
    def __init__(self):
        super(SpiderIP66, self).__init__()
        self.daemon = True


    def run(self):
        self.result = crawl()
