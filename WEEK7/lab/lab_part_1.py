def create_file():
    with open ('diary.txt', 'w') as f:
        f.write("2024-01-1 5: busy day with the project \n")
        f.write("2024-01-1: studied file handling in python \n")
        f.write("2024-01-1: finished first exercise \n")

create_file()

def add_entry(filename, date, content):
    with open (filename, 'a') as f: 
        f.write(f"{date}: {content}")

add_entry('diary.txt',"2024-01-18", "great day - finished first exercise")

def search_diary(filename, keyword):
    with open(filename, 'r') as f:
        file = f.readlines()
        lines =  []
        for line in file:
            if keyword in line:
                lines.append(line)
        return (lines)
import os

def safe_read_diary(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print ("File Not Found")







