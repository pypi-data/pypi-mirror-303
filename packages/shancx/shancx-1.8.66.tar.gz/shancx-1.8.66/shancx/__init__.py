#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/10/17 上午午10:40
# @Author : shancx
# @File : __init__.py
# @email : shanhe12@163.com

import os
def start():
    print("import successful")
# constants
import subprocess

__author__ = 'shancx'
 
__author_email__ = 'shanhe12@163.com'



# @Time : 2023/09/27 下午8:52
# @Author : shanchangxi
# @File : util_log.py
import time
import logging  
from logging import handlers



loggers = logging.getLogger()
loggers.setLevel(logging.INFO) 
log_name =  'project.log'
# mkDir(log_name)
logfile = log_name
time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename=logfile, when='D', encoding='utf-8')
time_rotating_file_handler.setLevel(logging.INFO)   
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
time_rotating_file_handler.setFormatter(formatter)
loggers.addHandler(time_rotating_file_handler)

from pathlib import Path
def crDir(path):
    path_obj = Path(path)
    directory = path_obj.parent if path_obj.suffix else path_obj
    directory.mkdir(parents=True, exist_ok=True)
 

def Tim_(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        loggers.info(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def validate_param_list(param_list):
    if len(param_list) == 0:
        raise ValueError("param_list cannot be empty.")    
    for sublist in param_list:
        if len(sublist) == 0:
            raise ValueError("Sub-lists in param_list cannot be empty.")        

from itertools import product
from concurrent.futures import ProcessPoolExecutor as PoolExecutor
def Mul_(map_fun,param_list,num=6):
    print(f"Pro num {num}")
    validate_param_list(param_list)
    if len(param_list) == 1:
        product_List = [(x,) for x in param_list[0]]
    else:
        product_List = list(product(*param_list))
    with PoolExecutor(num) as p:
        try:
           P_data = p.map(map_fun, product_List)
        except KeyboardInterrupt:
           sys.exit(1)  
    return list(P_data)

from concurrent.futures import ProcessPoolExecutor as PoolExecutor, as_completed 
import sys

def Mul_sub(task, param_list, num=6):
    print(f"Pro num {num}")
    validate_param_list(param_list)
    if len(param_list) == 1:
        product_list = [(x,) for x in param_list[0]]
    else:
        product_list = list(product(*param_list))
    with PoolExecutor(max_workers=num) as executor:
        try:
            futures = [executor.submit(task, item) for item in product_list]
            results = [future.result() for future in as_completed(futures)]
        except KeyboardInterrupt:
            sys.exit(1)    
    return results

def Mul_sub_S(task, param_list, num=6):
    print(f"Pro num {num}")
    validate_param_list(param_list)
    if len(param_list) == 1:
        product_list = [(x,) for x in param_list[0]]
    else:
        product_list = list(product(*param_list))
    results = [None] * len(product_list)

    with PoolExecutor(max_workers=num) as executor:
        futures = {executor.submit(task, item): idx for idx, item in enumerate(product_list)}        
        try:
            for future in as_completed(futures):
                idx = futures[future]
                results[idx] = future.result()
        except KeyboardInterrupt:
            sys.exit(1)    
    return results



def add_alias():
    command_to_add = "alias lt='ls -ltr'\n"
    bashrc_path = os.path.expanduser('~/.bashrc')
    with open(bashrc_path, 'a') as file:
        file.write(command_to_add)
    # 执行 source ~/.bashrc
    subprocess.run(['source', '~/.bashrc'], shell=True)

'''
from multiprocessing import Pool
'''
'''
 ##定義一個streamHandler
# print_handler = logging.StreamHandler()  
# print_handler.setFormatter(formatter) 
# loggers.addHandler(print_handler)
'''

"""
from main import makeAll,options
from multiprocessing import Pool
import datetime
from config import logger,output
import time
import pandas as pd
import os
from itertools import product
import threading

def excuteCommand(cmd):
    print(cmd)
    os.system(cmd)

def gpuPro(makeListUTC, isPhase, isDebug, gpu, isOverwrite):
    productList = product(makeListUTC, [isPhase], [isDebug], [gpu], [isOverwrite])

    with Pool(4) as p:
        p.map(makeAll, productList)

if __name__ == '__main__':
    cfg = options()
    isPhase = cfg.isPhase
    isDebug = cfg.isDebug
    sepSec = cfg.sepSec
    gpu = cfg.gpu
    pool = cfg.pool
    isOverwrite = cfg.isOverwrite
    timeList = pd.date_range(cfg.times[0], cfg.times[-1], freq=f"{sepSec}s")
    logger.info(f"时间段check {timeList}")
    gpuNum = 2
    eachGPU = 4

    makeListUTC = []
    for UTC in timeList:
        UTCStr = UTC.strftime("%Y%m%d%H%M")
        outpath = f"{output}/{UTCStr[:4]}/{UTCStr[:8]}/MSP2_WTX_AIW_QPF_L88_CHN_{UTCStr}_00000-00300-00006.nc"
        if not os.path.exists(outpath) or isOverwrite:
            makeListUTC.append(UTC)
    [print(element) for element in makeListUTC]

    phaseCMD = "--isPhase" if isPhase else ""
    debugCMD = "--isDebug" if isDebug else ""
    OverwriteCMD = "--isOverwrite"  
    gpuCMD = f"--gpu={gpu}"
    # cmdList = list(map(lambda x:f"python main.py --times={x.strftime('%Y%m%d%H%M')} {phaseCMD} {debugCMD} {OverwriteCMD} {gpuCMD}",makeListUTC))
    cmdList = list(map(lambda x:f"python main.py --times={x.strftime('%Y%m%d%H%M')} {phaseCMD} {debugCMD} {gpuCMD}",makeListUTC))

    with Pool(pool) as p:
        p.map(excuteCommand, cmdList)
"""


'''
# @Time : 2023/09/27 下午8:52
# @Author : shanchangxi
# @File : util_log.py
import time
import logging  
from logging import handlers
 
logger = logging.getLogger()
logger.setLevel(logging.INFO) 
log_name =  'project_tim_tor.log'
logfile = log_name
time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename=logfile, when='D', encoding='utf-8')
time_rotating_file_handler.setLevel(logging.INFO)   
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
time_rotating_file_handler.setFormatter(formatter)
logger.addHandler(time_rotating_file_handler)
print_handler = logging.StreamHandler()   
print_handler.setFormatter(formatter)   
logger.addHandler(print_handler)

'''

'''
###解决方法  pip install torch==2.4.0  torchvision    torchaudio三个同时安装  python 3.12  解决cuda启动不了的问题

Res网络
'''

'''
import concurrent.futures
from itertools import product
def task(args):
    args1,args2  = args
    print( f"Task ({args1}, {args2}) , result")
    return (args1,args2,5)

def Mul_sub(task, pro):
    product_list = product(*pro)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, item) for item in product_list]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]   
    return results
res = Mul_sub(task, [[1, 23, 4, 5], ["n"]])
print("res")
print(res)

'''

'''
    parser = argparse.ArgumentParser(description='shancx argparse ')
    parser.add_argument('--times', type=str, default='202408280000,202408281700')
    parser.add_argument('--pac', type=str, default='100000')
    parser.add_argument('--combine',action='store_true',default=False)
    config= parser.parse_args()
    print(config)
    config.times = config.times.split(",")
    config.pac = config.pac.split(",")
    if len(config.times) == 1:
        config.times = [config.times[0], config.times[0]]
    config.times = [datetime.datetime.strptime(config.times[0], "%Y%m%d%H%M"),
                    datetime.datetime.strptime(config.times[1], "%Y%m%d%H%M")]
    cfg = config

'''

