import sys
import os 
import pyglet 
import shutil 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def leave():
	sys.exit("Bye man, See you with more updates coming soon!")

def read():
	try:
		file=input("Please let us know the file name:")
		target = open(file, "r")  
		readfile = target.read()
		print(readfile)
	except Exception as e:
		print("There was a problem: %s" % (e))

def write():
	try:
		file = input("Enter file name: ")
		target = open(file, "a")
		while True:
			append = input()
			target.write(append)
			target.write("\n")
			if append.lower() == "menu":
				break
	except Exception as e:
		print("There was a problem: %s" % (e))



def delete():
    file = input("Enter file name: ")
    try:
        os.unlink(file)
    except Exception as e:
        print("There was a problem: %s" % (e))

def cd():
    try:
        print(os.getcwd())
        change = input("Change Y/N: ")
        if change.startswith("y"):
            path = input("New CWD: ")
            os.chdir(path)
    except Exception as e:
        print("There was a problem: %s" % (e))


def rename():
    try:
        file = input("Enter current file name: ")
        new = input("Enter new file name: ")
        shutil.move(file, new)
    except Exception as e:
        print("There was a problem: %s" % (e))


while True:
	
	print("Please choose your Options :\n\n1) Write to a file\n\n2) Read a File\n\n3) Delete a File\n\n4) Rename a file\n\n5) Change the Working Drectory('CD')\n\n6) Leave the editor ")
	ch=input("What do you think of doing ?")
	
	if ch == "1":
		write()
	elif ch == "2":
		read()
	elif ch == "4":
		rename()
	elif ch == "5":
		cd()
	elif ch == "3":
		delete()
	elif ch == "6":
		leave()
