import shutil
import os
import time
import subprocess

def Read():
    path=input("Enter the file path to read:")
    file=open(path,"r")
    print(file.read())
    input("Please enter...")
    file.close()

    def Write():
        path=input("Enter the path of the file you want to write or create:")
        if os.path.isfile(path):
            print("Rebuilding the existing file")
        else:
                print("Creating the new file")
                text=input("Write something:")
                file.open(path,"w")
                file.write(text)

                def Add():
                    file=input("Enter the file path")
                    text=input("Enter the text to add")
                    file.open(path,"a")
                    file.write('\n'+text)

                    def Delete():
                        path=input("Enter the file you want to delete")
                        if os.path.exists(path):
                            print("File found")
                            os.remove(path)
                            print("File has been deleted")
                        else:
                            print("File does not exist")

                            #List directories 
                            def Dirlist():
                                path=input("Enter the file directory path to display")
                                sortlist=sorted(os.listdir(path))
                                i = 0
                                while(i<len(sortlist)):
                                    print(sortlist[i]+'\n')
                                    i+=1

                                    def Check():
                                        fp=int(input('Check existence of\n 1.File \n 2.Directory\n'))
                                        if fp == 1:
                                            path=input("Enter the file path:")
                                            os.path.isfile(path)
                                            if os.path.isfile(path) == True:
                                                print("File found")
                                            else:
                                                print("File was not found")
                                                if fp == 2:
                                                    path=input("Enter the directory path:")
                                                    os.path.isdir(path)
                                                    if os.pah.isdir(path) == True:
                                                        print("Directory found")
                                                    else:
                                                        print("Directory not found")

                                                        def Move():
                                                            path1=input("Enter the source path of the file to move")
                                                            mr=int(input('\n Rename \n Move \n'))
                                                            if mr == 1:
                                                                path2=input("Enter the destination and the filename")
                                                                shutil.move(path1,path2)
                                                                print("File renamed")
                                                                if mr == 2:
                                                                    path2 = input("Enter the path to move")
                                                                    shutil.move(path1,path2)
                                                                    print("File moved successfully")

                                                                    def Copy():
                                                                        path = input("Enter the path of the file to copy or rename")
                                                                        path2=input("Enter the path to copy to:")
                                                                        shutil.copy(path1,path2)
                                                                        print("File copied successfully")

                                                                        def Makedir():
                                                                           path=input("Enter the path directory with the name \n eg C:\\users\Documents\mybooks\nWhere Newdir is new directory:")
                                                                           os.makedirs(path)
                                                                           print("Directory was successfully created")

                                                                           def Removedir():
                                                                               path=input("Enter the path of the directory you want to remove")
                                                                               treedir=int(input('\n 1.Deleted directory \n 2.Delete directory tree \n 3.Exit \n'))
                                                                               if treedir == 1:
                                                                                   os.rmdir(path)
                                                                                   if treedir == 2:
                                                                                       shutil.rmtree(path)
                                                                                       print("Directory was deleted sucesssfully")
                                                                                       if treedir == 3:
                                                                                           exit()

                                                                                           def Openfile():
                                                                                               path=input("Enter the apth of the file")
                                                                                               try:
                                                                                                   os.startfile(path)
                                                                                               except:
                                                                                                       print("File was not found")

                                                                                                       run=1
                                                                                                       while(run==1):
                                                                                                           try:
                                                                                                               os.system('clear')
                                                                                                           except OSError:
                                                                                                               os.system('cls')
                                                                                                               print("########File Manager in python 3.9#########")
                                                                                                               print("The current time and date is :",time.asctime())
                                                                                                               print('\n Choose the option number: \n')
                                                                                                               dec=int(input('"1.Read a file \n 2.Create a file \n 3. Append text to a file \n 4.Delete a file \n List files in a directory \n6.Check a file existence \n7 Move a file \n 8. Copy a file \n 9.Create a directory \n 10.Delete a directory \n11. Open a program\n 12.Exit" '))
                                                                                                               if dec==1:
                                                                                                                   Read()
                                                                                                                   if dec==2:
                                                                                                                       Write()
                                                                                                                       if dec==3:
                                                                                                                           Add()
                                                                                                                           if dec==4:
                                                                                                                               Delete()
                                                                                                                               if dec==5:
                                                                                                                                   Dirlist()
                                                                                                                                   if dec==6:
                                                                                                                                       Check()
                                                                                                                                       if dec==7:
                                                                                                                                           Move()
                                                                                                                                           if dec==8:
                                                                                                                                               Copy()
                                                                                                                                               if dec==9:
                                                                                                                                                   Makedir()
                                                                                                                                                   if dec == 10:
                                                                                                                                                       Removedir()
                                                                                                                                                       if dec == 11:
                                                                                                                                                           Openfile()
                                                                                                                                                           if dec == 12:
                                                                                                                                                               exit()
                                                                                                                                                               run=int(input("\n 1. Return to main menu \n 2.Exit \n"))
                                                                                                                                                               if run == 2:
                                                                                                                                                                   exit()

                                                                                                                                                                   #The project is complete let run now
