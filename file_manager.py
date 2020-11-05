#zad 8

class FileManager:
    def __init__(self,file_name):
        self.file_name = file_name

    def read_file(self):
        plik = open(self.file_name+".txt","r")
        zawartosc = plik.read()
        plik.close()
        return zawartosc

    def update_file(self,text_data):
        plik = open(self.file_name+".txt","a")
        plik.write(text_data)
        plik.close()

