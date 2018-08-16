import threading
import time

from proxy_spiders.spider_66ip import SpiderIP66
from proxy_spiders.spider_89ip import SpiderIP89
from proxy_spiders.spider_data5u import SpiderData5u
from proxy_spiders.spider_xicidaili import SpiderXicidaili
from proxy_spiders.spider_coderbusy import SpiderCoderBusy
from proxy_spiders.spider_kuaidaili import SpiderKuaidaili

from logic import logic_proxypool

THREAD_NUM = 20


class VerifyIP(threading.Thread):
    def __init__(self, ip):
        # 继承父类Tread的方法
        super(VerifyIP, self).__init__()
        self.ip = ip

    # 重写run方法
    def run(self):
        logic_proxypool.insert_into_proxypool(self.ip)


if __name__ == '__main__':
    while True:
        crawlers = [
            SpiderCoderBusy,
            SpiderIP66,
            SpiderIP89,
            SpiderData5u,
            SpiderXicidaili,
            SpiderKuaidaili
        ]
        result = []
        tasks = []
        for crawler in crawlers:
            task = crawler()
            task.setDaemon(True)
            tasks.append(task)
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()
        for task in tasks:
            try:
                result += task.result
            except:
                continue
        while len(result):
            for i in range(THREAD_NUM):
                if len(result) == 0:
                    break
                ip = result.pop(0)
                task = VerifyIP(ip)
                task.start()
            time.sleep(5)
