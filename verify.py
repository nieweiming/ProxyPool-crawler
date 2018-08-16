import threading
import time

from logic import logic_proxypool


class VerifyIP(threading.Thread):
    def __init__(self, ip_item):
        super(VerifyIP, self).__init__()
        self.ip_item = ip_item

    def run(self):
        logic_proxypool.verify_ip(self.ip_item)


if __name__ == '__main__':
    while True:
        for ip_items in logic_proxypool.load_unverified_ip():
            for item in ip_items:
                task = VerifyIP(item)
                task.start()
            time.sleep(5)
        time.sleep(300)
