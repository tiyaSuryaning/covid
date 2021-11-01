from tkinter import messagebox
from covid import Covid
from tkinter import *

covid = Covid(source="worldometers")
covid.get_data()

#italy = covid.get_status_by_country_name("italy")
#type(italy)

def covid_data(country):
    result = covid.get_status_by_country_name(country)
    if result:
        country = result['country']
        active = result['active']
        new_cases = result['new_cases']
        deaths = result['deaths']
        new_deaths = ['new_deaths']
        recovered = ['recovered']
        final = (country, active, new_cases, deaths, new_deaths, recovered)
        return final
    else:
        return None

def search():
    country = country_name.get()
    data = covid_data(country)
    if data:
        country_lbl['text'] = data[0]
        active_lbl['text'] = data[1]
        new_cases_lbl['text'] = data[2]
        deaths_lbl['text'] = data[3]
        new_deaths_lbl['text'] = data[4]
        recovered_lbl['text'] = data[5]
    else:
        messagebox.showerror('Error', 'Cannot find country {}'.format(country))

window = Tk()
window.title('Covid-19')
window.geometry('500x500')

country_name = StringVar()
country_name = Entry(window, textvariable=country_name)
country_name.pack()

search_btn = Button(window, text='Search', width=15, command=search)
search_btn.pack()

country_lbl = Label(window, text="", font=('bold',20))
country_lbl.pack()

active_lbl = Label(window, text="")
active_lbl.pack()

new_cases_lbl = Label(window, text="")
new_cases_lbl.pack()

deaths_lbl = Label(window, text="")
deaths_lbl.pack()

new_deaths_lbl = Label(window, text="")
new_deaths_lbl.pack()

recovered_lbl = Label(window, text="")
recovered_lbl.pack()


window.mainloop()