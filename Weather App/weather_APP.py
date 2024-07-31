from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from datetime import datetime

# Initialize the main window
w = Tk()
w.geometry('800x400')
w.title("Weather App")
w.resizable(0, 0)

def weather_data(query):
    try:
        res = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?{query}&units=metric&appid=a83c18cd432ec49ad4c0732c22bb5608'
        )
        res.raise_for_status()  # Raise an HTTPError for bad responses
        return res.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to get weather data: {e}")
        return None

def label(city):
    query = 'q=' + city
    w_data = weather_data(query)
    
    if not w_data or 'main' not in w_data:
        messagebox.showinfo("Error", "City not found or data unavailable!")
        return
    
    # Display weather information
    temp = w_data['main']['temp']
    description = w_data['weather'][0]['description']
    weather_main = w_data['weather'][0]['main']
    humidity = w_data['main']['humidity']
    pressure = w_data['main']['pressure']
    temp_max = w_data['main']['temp_max']
    temp_min = w_data['main']['temp_min']
    wind_speed = w_data['wind']['speed']
    
    # Determine the display settings based on the weather
    if temp > 10 and weather_main in ["Haze", "Clear"]:
        bcolor = "#F78954"
        fcolor = "white"
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/caleelsmith/Desktop/Menu/Weather App/sunny1.PNG"))
    elif temp > 10 and weather_main == "Clouds":
        bcolor = "#7492B3"
        fcolor = "white"
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/caleelsmith/Desktop/Menu/Weather App/cloudy1.PNG"))
    elif temp <= 10 and weather_main == "Clouds":
        bcolor = "#7492B3"
        fcolor = "white"
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/caleelsmith/Desktop/Menu/Weather App/cloudcold.PNG"))
    elif temp > 10 and weather_main == "Rain":
        bcolor = "#60789E"
        fcolor = "white"
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/caleelsmith/Desktop/Menu/Weather App/rain1.PNG"))
    elif temp <= 10 and weather_main in ["Fog", "Clear"]:
        bcolor = "white"
        fcolor = "black"
        imgWeather = ImageTk.PhotoImage(Image.open("/Users/caleelsmith/Desktop/Menu/Weather App/cold.PNG"))
    else:
        bcolor = "sky blue"
        fcolor = "black"
        imgWeather = None
    
    # Clear the previous display and set up the new one
    Frame(w, width=800, height=350, bg=bcolor).place(x=0, y=50)
    if imgWeather:
        Label(w, image=imgWeather, border=0).place(x=170, y=130)
    
    # Display weather details
    l2 = Label(w, text=f"{datetime.now():%B %d}", bg=bcolor, fg=fcolor, font=("Calibry", 25))
    l2.place(x=330, y=335)
    
    details = [
        f"Humidity: {humidity}%",
        f"Pressure: {pressure} hPa",
        f"MIN Temp: {temp_min}°C",
        f"MAX Temp: {temp_max}°C",
        f"Wind Speed: {wind_speed} m/s",
        f"{temp}°C"
    ]
    
    for idx, detail in enumerate(details):
        l3 = Label(w, text=detail, bg=bcolor, fg=fcolor, font=("Calibry", 12))
        l3.place(x=510, y=95 + 40 * idx)

def on_entry(e):
    e1.delete(0, 'end')

def on_leave(e):
    if e1.get() == '':
        e1.insert(0, 'Search City')

# Frame for the title
Frame(w, width=800, height=50, bg='#353535').place(x=0, y=0)

# Search bar
imgSearch = ImageTk.PhotoImage(Image.open("/Users/caleelsmith/Desktop/Menu/Weather App/search.PNG"))
e1 = Entry(w, width=21, fg='white', bg='#353535', border=0, font=('Calibry', 12))
e1.bind("<FocusIn>", on_entry)
e1.bind("<FocusOut>", on_leave)
e1.insert(0, 'Search City')
e1.place(x=620, y=15)

def cmd1():
    city = e1.get().strip()
    if city:
        label(city)

Button(w, image=imgSearch, command=cmd1, border=0).place(x=750, y=10)

# Initial weather data display for a default city
label("Los Angeles")

w.mainloop()