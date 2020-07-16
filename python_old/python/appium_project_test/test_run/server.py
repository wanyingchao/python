# coding = utf-8
from test_run.doc_cmd import DosCmd
from test_run.port import Port
from test_run.write_user_command import WriteUserCommang


class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.write_file = WriteUserCommang()

    def get_devices(self):
        '''获取设备信息'''
        devices_list = []
        result_list = self.dos.excute_cmd_result("adb devices")
        if len(result_list) >= 2:
            for i in result_list:
                if "List" in i:
                    continue
                devices_info = i.split("\t")
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        return None

    def creat_port_list(self,start_port):
        '''创建可用端口'''
        port = Port()
        port_list = []
        port_list = port.creat_port_list(start_port,self.device_list)
        return port_list

    def  creat_command_list(self,i):
        # appium -p 4700 -bp 4701 -U 127.0.0.1:52001
        command_list = []
        appium_port_list = self.creat_port_list(4700)
        bootstrap_port_list = self.creat_port_list(4900)
        device_list = self.device_list
        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " +device_list[i] + " --no-reset --session-override"
        command_list.append(command)
        self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))
        return command_list

    def start_server(self,i):
        '''启动服务'''
        self.start_list = self.creat_command_list(i)
        self.dos.excute_cmd(self.start_list[0])

    def kill_server(self):
        server_list = self.dos.excute_cmd_result("tasklist | find 'node.exe'")
        if len(server_list) > 0:
            self.dos.excute_cmd("taskkill -F -PID node.exe")


if __name__ == '__main__':
    server = Server()