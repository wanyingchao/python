import subprocess
from time import ctime


def appium_start(host, port,device):
    cmd = 'start /b appium -a '+ host+ ' -p '+ str(port)+ ' -U '+ device

    print('%s at %s' %(cmd,ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open('./appium_log/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = "4723"
    device = '621QECQ63KZTB'
    appium_start(host, port, device)