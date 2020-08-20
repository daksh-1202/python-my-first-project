import os
x=input("hello, how are you ?, I am fine. \n ")
while True:
        p=input ("what do you want me to open ?")
        if ((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("chrome" in p) or( "browser " in p)or ("google" in p ))):                os.system("start chrome")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("notepad" in p) or( "editor " in p)or ("text editor" in p ))):                os.system("start notepad")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("my computer" in p) or( "computer  " in p)or ("windows explorer" in p ))):                os.system("start explorer.exe")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("calc" in p) or( "mathematicla operator " in p)or ("calculator" in p ))):                os.system("start calc")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("recyclebin" in p) or( "trash" in p)or ("bin" in p ))):                os.system("start shell:RecycleBinfolder")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("command prompt" in p) or( "cmd" in p)or ("CLI" in p ))):                os.system("start cmd")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("shell python" in p) or( "idle python" in p)or ("live interpreter shell" in p ))):                os.system("start idle.exe")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("python" in p) or( "python" in p)or ("live interpreter" in p ))):                os.system("start python.exe")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and (("windows media player " in p) or( "media player " in p)or ("song player" in p ))):       os.system("start wmplayer")
        elif((("open"in p)or("execute" in p )or("start" in p ) or("run" in p )) and ((" windows controler " in p) or( "controler " in p)or ("control panel" in p ))):          os.system("start control")
        elif(("quit" in p)or ("break" in p )or ( " stop" in p ) or ("bye " in p )):                break
        else:                print("pls enter valid names !thank you .")
