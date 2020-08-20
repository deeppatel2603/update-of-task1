import os
import time
import webbrowser
currentTime = time.strftime('%H:%M') 
if currentTime < "12" :
    print(       "good morning!!")
    print("date:",time.strftime("%Y-%m-%d"),"time:",time.strftime("%H:%M:%S"))
if currentTime > "12" and currentTime <"17":
    print(       "good afternoon!!")
    print("date:",time.strftime("%Y-%m-%d"),"time:",time.strftime("%H:%M:%S")) 
if currentTime > "18" :
    print(       "good evening!!")
    print("date:",time.strftime("%Y-%m-%d"),"time:",time.strftime("%H:%M:%S"))
x=input("how can i help u:")
os.system(x)
if "hi" in x or "hello" in x:
    print("hello,how are u?")
if ("open" in x) and ("youtube" in x) or ("play song" in x):
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = "https://www.youtube.com"
    webbrowser.get(browser_path).open(url)
if "what "in x or"can" in x and "you do" in x:
    print("1.run chrome\n","2.run notepad\n","run youtube","4.run media player\n","5.read file\n","6.write file\n","6.copy file\n")
if  ("chrome"in x) or ("google"in x):
    os.system("chrome")
    
if ("notepad"in x) or ("editor"in x):
    os.system("notepad")
if ("run"in x) or ("player"in x) and ("media"in x):
    os.system("wmplayer")
if ("read"in x) or ("scan" in x) and ("file"in x) or ("textfile" in x):
    y=input("enter the name of file with extension (.txt):")
    f=open(y,'r')
    print(f.read())
if ("write"in x) or ("create" in x) and ("file"in x) or ("textfile" in x): 
    y=input("file name to be created (.txt):")
    f=open(y,'w')
    z=input("what u want to write:")
    #note:write will remove previous data of file
    print(f.write(z))
if ("copy" in x) or ("select"in x) and("file" in x) or ("data" in x):
    r=input ("enter file name from where data need to be copied(.txt):")
    u=input ("enter file name where data need to be copied(.txt):") 
    f=open(r,'r')
    f1=open(u,'w')
    for data in f:
        f1.write(data)
else:
    print("not found or closed:" + x)