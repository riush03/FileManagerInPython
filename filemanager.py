import os
import time

class FileMananger:
    def __init__(self,f_name:str,f_mode="a+"):
        self.f_name = f_name
        self.f_mode = f_mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.f_name,self.f_mode)
            return self
        except:
            self.createFile()
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def createFile(self):
        if os.path.isfile(self.f_name):
            pass
        else:
            create_file = self.file = open(self.f_name,"w+")
            if create_file:
                print(f"Created `{self.f_name}` file. \n File mode ` {self.f_mode} .")

    def deleteFile(self):
        file_to_del = os.remove(self.f_name)
        if file_to_del == None:
            print(f"Removed `{self.f_name}` file.")

    def writeToFile(self,txt):
        if self.file.closed == False:
            self.file.write(txt)
            print(f"`{txt}` added to `{self.f_name}` .")

    def readFile(self):
        if self.file.closed == False and os.path.isfile(self.f_name):
            lines = self.file.readlines()
            items: list = list()
            for line in lines:
                item = line.split(';')
                items.append({"name":item[0],"price":item[1],"quantity":item[2]})

            return items

if __name__ == "__main__":
    file_mananger = FileMananger("log.txt", "r+")
    file_mananger.createFile()
    with file_mananger as fs:
        fs.writeToFile("Indomie;40;2\n")
    with file_mananger as flm:
        my_shopping_list = flm.readFile()
    print(my_shopping_list)
    time.sleep(7)
    file_mananger.deleteFile()