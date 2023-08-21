import tkinter as tk
import time
import os
from weather import data, update_weather_data, store_parameters, parameters, data_check

# Updates data for GUI based on user search
def weather_search():
    # Gets query from search bar
    city_query = ent_select.get()
    # Saves parameters for use when restarting application
    store_parameters(city_query, parameters)
    # Checks for correct data
    in_file = data_check()
    current_time = time.time()
    # Modified timestamp for 'weather.json'
    mod_time = os.path.getmtime('weather.json')
    # new_data to be used for the GUI update
    new_data = update_weather_data(city_query, in_file, current_time, mod_time, parameters)

    # updating variables
    temperature = new_data['current']['temperature']
    city = new_data['location']['name']
    state = new_data['location']['region']
    uv_index = new_data['current']['uv_index']
    humidity = new_data['current']['humidity']
    wind_dir = new_data['current']['wind_dir']
    wind_speed = new_data['current']['wind_speed']

    # Configuring widgets to use updated data
    lbl_temp.config(text='{}\u00b0 F'.format(temperature))
    lbl_city_state.config(text='{}, {}'.format(city, state))
    lbl_uv_value.config(text=uv_index)
    lbl_humidity_value.config(text='{}%'.format(humidity))
    lbl_wind_dir_value.config(text=wind_dir)
    lbl_wind_spd_value.config(text=wind_speed)


# Variables are assigned from data saved for application start
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

ent_select = tk.Entry(master=frm_select, width=30)
ent_select.grid(row=0, column=0)
ent_select.insert(0, 'Select City (City, Region(State))')

btn_search = tk.Button(master=frm_select, width=7, text='Search', command=weather_search)
btn_search.grid(row=0, column=1)

frm_main = tk.Frame(master=window)
frm_main.grid(row=1, column=0)
lbl_temp = tk.Label(master=frm_main, text='{}\u00b0 F'.format(temperature),   # '\u00b0' is degree symbol
                    font=('arial', 30))
lbl_temp.grid(row=0, column=0)
lbl_city_state = tk.Label(master=frm_main, text='{}, {}'.format(city, state), font='arial')
lbl_city_state.grid(row=1, column=0)

frm_lower = tk.Frame(master=window)
frm_lower.grid(row=2, column=0)

# First row of misc widgets
# Displaying uv index
frm_uv = tk.Frame(master=frm_lower)
frm_uv.grid(row=0, column=0)
lbl_uv = tk.Label(master=frm_uv, text='UV Index')
lbl_uv.grid(row=0, column=0)
lbl_uv_value = tk.Label(master=frm_uv, text=uv_index)
lbl_uv_value.grid(row=1, column=0)

# Displaying humidity percentage
frm_humidity = tk.Frame(master=frm_lower)
frm_humidity.grid(row=0, column=1)
lbl_humidity = tk.Label(master=frm_humidity, text='Humidity')
lbl_humidity.grid(row=0, column=1)
lbl_humidity_value = tk.Label(master=frm_humidity, text='{}%'.format(humidity))
lbl_humidity_value.grid(row=1, column=1)

# Final row of misc widgets
# Displaying wind speed
frm_wind_spd = tk.Frame(master=frm_lower)
frm_wind_spd.grid(row=1, column=0)
lbl_wind_spd = tk.Label(master=frm_wind_spd, text='Wind Speed')
lbl_wind_spd.grid(row=2, column=0)
lbl_wind_spd_value = tk.Label(master=frm_wind_spd, text=wind_speed)
lbl_wind_spd_value.grid(row=3, column=0)

# Displaying wind direction
frm_wind_dir = tk.Frame(master=frm_lower)
frm_wind_dir.grid(row=1, column=1)
lbl_wind_dir = tk.Label(master=frm_wind_dir, text='Wind Direction')
lbl_wind_dir.grid(row=2, column=1)
lbl_wind_dir_value = tk.Label(master=frm_wind_dir, text=wind_dir)
lbl_wind_dir_value.grid(row=3, column=1)

# Configuring padding of widgets for visual appeal
for widget in frm_lower.winfo_children():
    widget.grid_configure(padx=15, pady=30)

window.mainloop()
