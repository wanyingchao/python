ControlFocus("打开","","Edit1")
;Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)
ControlSetText("打开","","Edit1","D:\Users\wyc\Photo\123.jpg")
Sleep(2000)
ControlClick("打开","","Button1")