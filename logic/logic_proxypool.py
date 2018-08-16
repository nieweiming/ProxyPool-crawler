import requests
import time
import json

from models import proxypool
from logger.error_log import error_log
from logger.info_log import info_log


def is_available(ip):
    """
    检验IP是否可用
    :param ip:
    :return:
    """
    proxies = {
        'http': 'http://%s' % ip,
        'https': 'http://%s' % ip
    }
    try:
        res_data = requests.get('https://www.nyloner.cn/checkip',
                                proxies=proxies, timeout=5).json()
        remote_ip = res_data['remote_ip']
    except:
        return False
    if remote_ip in ip:
        return True
    return False


def insert_into_proxypool(ip):
    """
    代理池中插入ip
    :param ip:
    :return:
    """
    status = is_available(ip)
    if not status:
        return
    ip_item = {
        'ip': ip.split(':')[0],
        'ip_port': ip.split(':')[-1],
        'ctime': int(time.time()),
        'utime': int(time.time())
    }
    try:
        proxypool.insert_into_proxypool(ip_item)
    except Exception as e:
        error_log.error('insert_into_proxypool fail.[ip_item]={} [msg]={}'.format(json.dumps(ip_item), e))
        return
    info_log.info('insert_into_proxypool success.[ip_item]={}'.format(json.dumps(ip_item)))


def verify_ip(ip_item):
    """
    验证ip信息
    :param ip_item:
    :return:
    """
    status = is_available('%s:%s' % (ip_item['ip'], ip_item['ip_port']))
    if status:
        ip_item['utime'] = int(time.time())
        try:
            proxypool.update_ip(ip_item)
        except Exception as e:
            error_log.error('update_ip fail.[item]={} [msg]={}'.format(json.dumps(ip_item), e))
            return
        info_log.info('update_ip success.[ip_item]={}'.format(json.dumps(ip_item)))
    else:
        try:
            proxypool.delete_ip(ip_item)
        except Exception as e:
            error_log.error('delete_ip fail.[item]={} [msg]={}'.format(json.dumps(ip_item), e))
            return
        info_log.info('delete_ip success.[ip_item]={}'.format(json.dumps(ip_item)))


def load_unverified_ip():
    '''加载未通过验证的ip'''
    ip_items = proxypool.get_all_ip()
    items = []
    for item in ip_items:
        items.append(item)
        if len(items) < 20:
            continue
        yield items
        items = []
    yield items
