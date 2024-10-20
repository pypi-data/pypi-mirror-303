from os import system
from os.path import exists,expanduser

with open(f"{__file__[:-6]}intros/README.md", "r", encoding="utf-8") as fh:
    readmetxt = fh.read()
with open(f"{__file__[:-6]}/intros/LICENSE", "r", encoding="utf-8") as fh:
    licensetxt = fh.read()

def readme():print(readmetxt)
def license():print(licensetxt)

def run():
    while True:
        exec(input("(roulette)>>> ") + "()")

def install():
    if exists(expanduser("~/.local/bin/tdb")) or system(f"cp {__file__[:-6]}tdb ~/.local/bin/tdb") or system(f"mkdir ~/.local/lib/tdb") or system(f"cp {__file__[:-6]}tdb.py ~/.local/lib/tdb/"):
        print("Error: Already Installed TDB")
    else:
        print("Successfully Configured TDB")