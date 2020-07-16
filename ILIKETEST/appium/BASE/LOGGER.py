import logging


def get_log():
    # 配置日志参数
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 日志文件保存路径
    logfile = 'E:/python/ILIKETEST/appium/Report/logs/runlog.log'
    # 日志输出到文件
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.INFO)
    # 日志输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # 设置日志输出格式
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


logger = get_log()
