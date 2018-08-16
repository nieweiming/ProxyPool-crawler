# -*- coding: utf-8 -*-
# @Desc: 日志记录

import logging
import os

logger_name = "info_log"
info_log = logging.getLogger(logger_name)
info_log.setLevel(logging.INFO)

try:
    os.mkdir('./log_files')
except:
    pass

log_path = "./log_files/info_log.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.INFO)

fmt = "[Date: %(asctime)-15s][Level: %(levelname)s]" \
      "[File: %(filename)s][LineNo: %(lineno)d][Process: %(process)d]%(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

fh.setFormatter(formatter)
info_log.addHandler(fh)
