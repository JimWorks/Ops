# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      logger
   Description:
   Author:          Administrator
   date：           2018/6/2
-------------------------------------------------
   Change Activity:
                    2018/6/2:
-------------------------------------------------
"""
import logging
from logging.config import fileConfig
from Ops.settings import BASE_DIR
import os


logger_file = os.path.join(BASE_DIR, 'conf', 'logger.conf')
print(logger_file)

fileConfig(logger_file)
scanhost_logger = logging.getLogger('scanhost')
ansible_logger = logging.getLogger('ansible')
user_logger = logging.getLogger('user')
