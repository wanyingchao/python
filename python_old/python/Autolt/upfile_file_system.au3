ControlFocus("��","","Edit1")
;Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)
ControlSetText("��","","Edit1","D:\Users\wyc\Photo\ͼ4.zip")
Sleep(2000)
ControlClick("��","","Button1")