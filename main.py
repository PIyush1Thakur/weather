from tkinter import *
import requests
from bs4 import BeautifulSoup


def connect():
    urls = search.get().strip().lower()
    label.config(text="Loading...", fg="yellow")
    label1.config(text="")
    responses = requests.get(f"https://www.timeanddate.com/weather/india/{urls}")

    if responses.status_code == 200:
        soup = BeautifulSoup(responses.content, 'html.parser')
        tr_element = soup.find("tr", class_="h2")
        tr_element2 = soup.find("tr", class_="h2 soft")

        if tr_element and tr_element2:
            row_data = [td.text for td in tr_element.find_all("td")]
            row_data2 = [td.text for td in tr_element2.find_all("td")]
            label.config(text=" | ".join(row_data),fg="black")
            label1.config(text=" | ".join(row_data2))
        else:
            label.config(text="Weather Data Not Found", fg="red")
            label1.config(text="")
    else:
        label.config(text="Invalid Location", fg="red")
        label1.config(text="")

def about():
    about_dis = Tk()
    about_dis.title("About")
    about_dis.resizable(False, False)
    about_dis.configure(background="black")
    about_dis.geometry("150x70")
    lab = Label(about_dis, text="About: 1.0.v \nDeveloped by Piyush", fg="white",bg='black')
    lab.pack()



load = Tk()
load.title('Get Weather')
load.geometry("600x400")
load.config(bg='#121212')
load.resizable(False, False)
# Top Frame (Search Bar)
up_frame = Frame(load, bg='#121212')
up_frame.pack(pady=20)


down_frame = Frame(load, bg='#E0E0E0')
down_frame.pack(pady=0, fill='both', expand=True)


search = Entry(up_frame, bg='#1F1F1F', fg='#FFFFFF', font=('Arial', 14), width=20, insertbackground="white")
search.pack(pady=10)




button1 = Button(load, text="ℹ️", bg='black', fg='white', font=('Arial', 5, 'bold'), command=about)
button1.place(x=566,y=0)

button = Button(up_frame, text="Search", bg='#007BFF', fg='white', font=('Arial', 12, 'bold'), command=connect)
button.pack(pady=5)


label = Label(down_frame, text="", bg='#E0E0E0', fg='black', font=('Arial', 12, 'bold'))
label.pack(pady=10)

label1 = Label(down_frame, text="", bg='#E0E0E0', fg='black', font=('Arial', 12))
label1.pack(pady=10)

load.mainloop()
