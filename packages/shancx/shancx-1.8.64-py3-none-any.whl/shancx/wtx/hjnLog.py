import datetime
import os
import time
import traceback
import logging

class waitHJN():

    def __init__(self,logger,sepSec,timeoutSec):

        if not isinstance(logger,logging.Logger):
            self.logger=self.initLog()
        else:
            self.logger=logger
        self.sepSec=sepSec
        self.timeoutSec=timeoutSec

    def initLog(self):
        logger = logging.getLogger("hjn_example")
        logger.setLevel(logging.DEBUG)
        # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s|%(levelname)8s|%(process)d|%(filename)16s[:%(lineno)d]|%(message)s')
        ch.setFormatter(formatter)
        # 将相应的handler添加在logger对象中
        logger.addHandler(ch)
        return logger



    def action(self,path):
        pass

    def wait(self,path,debug=False):
        t0 = datetime.datetime.now()
        t1 = datetime.datetime.now()
        flag= True
        while flag:
            if (t1-t0).total_seconds()>self.timeoutSec:
                flag =False
                break
            else:
                if os.path.exists(path):
                    try:
                        self.action(path)
                        flag =False
                        return True
                    except Exception as e:
                        self.logger.error(traceback.format_exc())
                        self.logger.error(f"wrong data{path}")

                if not debug:
                    self.logger.info(f"{path} missing  waiting {self.sepSec}s {int(self.timeoutSec-(t1-t0).total_seconds())}s remain")
                    time.sleep(self.sepSec)
                else:
                    self.logger.info(f"{path} missing  break")
                    return False
                t1 = datetime.datetime.now()

        if not flag:
            return False
        else:
            return True


class wait1(waitHJN):

    def action(self,path):
        os.path.exists(path)



if __name__ == '__main__':

    a = wait1("",2,10)
    print(a.wait("./test.csv"))
