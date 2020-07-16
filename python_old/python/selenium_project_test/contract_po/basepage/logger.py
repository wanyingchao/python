import logging


def get_log():
    # 配置日志参数
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logfile = 'E:/python/yusuan_PO/report/logs/runlog.log'

    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


logger = get_log()