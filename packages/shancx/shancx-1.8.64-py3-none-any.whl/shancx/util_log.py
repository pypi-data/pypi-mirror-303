
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/09/27 下午8:52
# @Author : shanchangxi
# @File : util_log.py

import logging  # 引入logging模块
from logging import handlers
# from util.util_dir import *

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级开关

# 第二步，创建一个handler，用于写入日志文件
log_name =  'project.log'
logfile = log_name

time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename=logfile, when='D', encoding='utf-8')
time_rotating_file_handler.setLevel(logging.INFO)  # 输出到file的log等级的开关

# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
time_rotating_file_handler.setFormatter(formatter)

# 第四步，将handler添加到logger里面
logger.addHandler(time_rotating_file_handler)

# 如果需要同時需要在終端上輸出，定義一個streamHandler
print_handler = logging.StreamHandler()  # 往屏幕上输出
print_handler.setFormatter(formatter)  # 设置屏幕上显示的格式
logger.addHandler(print_handler)
