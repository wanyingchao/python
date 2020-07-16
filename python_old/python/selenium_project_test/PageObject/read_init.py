# coding=utf-8
import configparser  # 解析配置文件的模块


class ReadIni():

    def __init__(self, file_path=None):

        if file_path is None:
            self.file_path = 'E:/python/PageObject/Login/new_contract.ini'
        else:
            self.file_path = file_path
        self.cf = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read(self.file_path, encoding='utf-8')  # 配置文件的路径
        return cf

    # 通过key获取对应的value
    def get_value(self, key, node=None):
        if node == None:
            node = "newcontract"
        try:
            data = self.cf.get(node, key)
        except:
            data = None
        return data


if __name__ == '__main__':
    # read_ini = ReadIni('G:/project/web/config/data1.ini')
    read_ini = ReadIni()
    print(read_ini.get_value('contractname'))
    # print(read_ini.get_value("user_phone", "input_data"))
