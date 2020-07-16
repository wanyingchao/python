ControlFocus("打开","","Edit1")
;Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)
ControlSetText("打开","","Edit1","C:\Users\wyc\Desktop\样例图\纸质合同样例\纸质合同照片01.png")
Sleep(2000)
ControlClick("打开","","Button1")