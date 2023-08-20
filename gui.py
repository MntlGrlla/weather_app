import tkinter as tk
from weather import data, parameters

temperature = data['current']['temperature']
city = data['location']['name']
state = data['location']['region']
uv_index = data['current']['uv_index']
humidity = data['current']['humidity']
wind_dir = data['current']['wind_dir']
wind_speed = data['current']['wind_speed']

window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=250)
window.title('MyWeather')

frm_select = tk.Frame(master=window)
frm_select.grid(row=0, column=0)

ent_select = tk.Entry(master=frm_select, width=35)
ent_select.pack()
ent_select.insert(0, 'Select City (City, Region(State))')

frm_main = tk.Frame(master=window)
frm_main.grid(row=1, column=0)
lbl_temp = tk.Label(master=frm_main, text='{}\u00b0 F'.format(temperature), font=('arial', 30))  # '\u00b0' is degree symbol
lbl_temp.grid(row=0, column=0)
lbl_city_state = tk.Label(master=frm_main, text='{}, {}'.format(city, state), font='arial')
lbl_city_state.grid(row=1, column=0)

frm_lower = tk.Frame(master=window)
frm_lower.grid(row=2, column=0)

frm_uv = tk.Frame(master=frm_lower)
frm_uv.grid(row=0,column=0)
lbl_uv = tk.Label(master=frm_uv, text='UV Index')
lbl_uv.grid(row=0, column=0)
lbl_uv_value = tk.Label(master=frm_uv, text=uv_index)
lbl_uv_value.grid(row=1, column=0)

frm_humidity = tk.Frame(master=frm_lower)
frm_humidity.grid(row=0, column=1)
lbl_humidity = tk.Label(master=frm_humidity, text='Humidity')
lbl_humidity.grid(row=0, column=1)
lbl_humidity_value = tk.Label(master=frm_humidity, text=humidity)
lbl_humidity_value.grid(row=1, column=1)

frm_wind_spd = tk.Frame(master=frm_lower)
frm_wind_spd.grid(row=1, column=0)
lbl_wind_spd = tk.Label(master=frm_wind_spd, text='Wind Speed')
lbl_wind_spd.grid(row=2, column=0)
lbl_wind_spd_value = tk.Label(master=frm_wind_spd, text=wind_speed)
lbl_wind_spd_value.grid(row=3, column=0)

frm_wind_dir = tk.Frame(master=frm_lower)
frm_wind_dir.grid(row=1, column=1)
lbl_wind_dir = tk.Label(master=frm_wind_dir,  text='Wind Direction')
lbl_wind_dir.grid(row=2, column=1)
lbl_wind_dir_value = tk.Label(master=frm_wind_dir, text=wind_dir)
lbl_wind_dir_value.grid(row=3, column=1)

for widget in frm_lower.winfo_children():
    widget.grid_configure(padx=15, pady=30)

window.mainloop()
