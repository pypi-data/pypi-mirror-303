from pyotp import TOTP
from os import system
from argparse import ArgumentParser as AP
from os.path import exists
from datetime import date,datetime

if __name__ != "__main__":
    print("Warning: Direct Access TDB in Python IDLE is Deprecated,Please Read Readme to Get More Information.")
    exit(1)

parser = AP(usage="tdb [operation] [file]")
parser.add_argument("-o",help="the operation to the file",required=True,type=str)
parser.add_argument("-f",help="the file that you want to operate",required=True,type=str)
arg = parser.parse_args()
mode = arg.o
file = arg.f
filepath = __file__[:-6] + file + ".txt"
if mode == "new" and exists(filepath):
    if input("Warning: The File is Already Exist!(Press [ENTER] to Stop Create New File,Enter Any Character to Skip) "):pass
    else:exit()
if mode != "list" and mode != "rmdb" and mode != "dumpdb":
    try:
        if mode == "recover" or mode == "readbak":
            with open(filepath + ".bak","r",encoding="utf-8") as bak:text = bak.read()
        if mode != "new" and mode != "recover" and mode != "readbak" and mode != "removebak" or mode == "backup":
            with open(filepath,"r",encoding="utf-8") as fr:text = fr.read()
        if mode == "new" or mode == "recover" or mode == "write":fw = open(filepath,"w",encoding="utf-8")
        if mode == "write" or mode == "backup":bak = open(filepath + ".bak","w",encoding="utf-8")
    except FileNotFoundError:
        print("Error: File not exist!")
        exit()
def read(skip = False):
    if "tt" in file and not skip:print(TOTP(text).now())
    else:print(text)

def write():
    read(True)
    bak.write(text)
    newids = []
    newid = input(">>> ")
    while newid:
        newids.append(newid)
        newid = input(">>> ")
    for ind,id in enumerate(newids[:-1]):newids[ind] = id + "\n"
    fw.writelines(newids)
    fw.close()
    bak.close()

def recover():
    if int(input(f"Backup:\n{text}\nAre You Sure(Yes:1,No:0)? ")):
        system(f"rm -rf {filepath + '.bak'}")
        fw.write(text)
    fw.close()

def new():
    fw.close()

def remove():
    system(f"rm -rf {filepath}")

def removebak():
    system(f"rm -rf {filepath + '.bak'}")

def readbak():
    if "tt" in file:print(TOTP(text).now())
    else:print(text)

def backup():
    bak.write(text)

def list():
    system(f"ls {__file__[:-6]} | grep .txt")

def rmdb():
    if input("If TDB Has Any Issue,Please Upload it to My Email:kill114514251@outlook.com.If You Really Want to Remove TDB,Enter \"isiwrmdb\"(This Operation Will Also Remove This Package With the PIP): ") == "isiwrmdb":
        system("rm -rf ~/.local/lib/tdb")
        system("rm -rf ~/.local/bin/tdb")
        system("pip3 uninstall textdatabase")
        print("Successfully Removed TDB")

def dumpdb():
    system("cp -r ~/.local/lib/tdb ~/tdb" + str(date.today()) + "_" + str(datetime.now().time())[:-7].replace(":","-"))
    print("Successfully Backed up TDB")

if mode == "readkey":read(True)
else:exec(mode + "()")