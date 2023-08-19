import tkinter as tk
from weather import data, parameters

temperature = data['current']['temperature']
city = data['location']['name']
state = data['location']['region']

window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=150)
frm_main = tk.Frame(bg='black', width=100, height=200)
frm_main.grid(column=0)
lbl_temp = tk.Label(
    master=frm_main,
    text='{}\u00b0 F'.format(temperature),  # '\u00b0' is degree symbol
    bg='blue',
    fg='white',
    font=('arial',30)
)
lbl_temp.pack()
lbl_city_state = tk.Label(
    master=frm_main,
    text='{}, {}'.format(city, state),
    bg='yellow',
    fg='black',
    font='arial'
)
lbl_city_state.pack()


window.mainloop()