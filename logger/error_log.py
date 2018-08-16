# -*- coding: utf-8 -*-
# @Desc: 日志记录

import logging
import os

logger_name = "error_log"
error_log = logging.getLogger(logger_name)
error_log.setLevel(logging.WARNING)

try:
    os.mkdir('./log_files')
except:
    pass
log_path = "./log_files/error_log.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

fmt = "[Date: %(asctime)-15s][Level: %(levelname)s]" \
      "[File: %(filename)s][LineNo: %(lineno)d][Process: %(process)d]%(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

fh.setFormatter(formatter)
error_log.addHandler(fh)
