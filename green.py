import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
import threading
from tkVideoPlayer import TkinterVideo
import customtkinter
import serial
# root
root = tk.Tk()
root.geometry("800x480")
root.title("Green House")
root.iconbitmap("plant_icon.ico")
style = ttk.Style("simplex")
# frame
main_frame=ttk.Frame(root)
main_frame.pack(fill=BOTH,expand=True) 

# value read
# ser = serial.Serial('COM4', 9600, timeout=1)
# global modified
# global values

# def read():
#     global my_img1
#     global my_img2
#     global my_img3
#     global my_img4
#     global my_img5
#     global my_img6
#     global Fan_label
#     global Light_label
#     global Tap_label
#     global values
#     global modified
#     global soil_moisture
#     global temperature
#     global Humidity
#     global light
#     global Soil_Temperature
#     global label3
#     global plant_label
#     global Fan_on
#     global Tap_on
#     global Light_on
#     global Fan_off
#     global Light_off
#     global Tap_off
#     global Fan_ON
#     global Tap_ON
#     global Light_ON

    
#     try:
#         line = ser.readline().decode()   # read a byte
#         sensor=line.split(",")
#         modified = []
#         values = []
#         for line in sensor:
#             modified.append(line.strip())
#         print(sensor)
#         if len(modified) == 5:
#             values.append(modified)
#             soil_moisture = values[0][0]
#             temperature = values[0][1]
#             Humidity = values[0][2]
#             light = values[0][3]
#             Soil_Temperature = values[0][4]
#             Temp.configure(amountused=temperature)
#             Hum.configure(amountused=Humidity)
#             Soil.configure(amountused=Soil_Temperature)
#             Mois.configure(amountused=soil_moisture)
#             Light.configure(amountused=light)
#             temperature=float(temperature)
#             soil_moisture=int(soil_moisture)
#             if temperature > 18 and temperature < 25 and soil_moisture > 50:
#                 print ("ok")
#                 plant_label.configure(text="GOOD CONDITION")
#             elif temperature < 18:
#                 Tap_label.configure(image=Tap_OFF)
#                 plant_label.configure(text="Maintain Temperature")
#                 Light_label.configure(image=Light_ON)
#             elif temperature > 25:
#                 plant_label.configure(text="Maintain Temperature")
#                 Fan_label.configure(image=Fan_ON)
#             elif soil_moisture > 50:
#                 print("Water Is Off")
#                 Tap_label.configure(image=Tap_OFF)
#                 plant_label.configure(text="Good Condition")
#             elif soil_moisture < 50:
#                 plant_label.configure(text="Water Is On")
#                 Tap_label.configure(image=Tap_ON)
          





    
            
#     except Exception as e:
#         line = ser.readline().decode()   # read a byte
#         sensor=line.split(",")
#         modified = []
#         values = []
#         for line in sensor:
#             modified.append(line.strip())
#         print(sensor)
#         if len(modified) == 5:
#             values.append(modified)
#             soil_moisture = values[0][0]
#             temperature = values[0][1]
#             Humidity = values[0][2]
#             light = values[0][3]
#             Soil_Temperature = values[0][4]
#             Temp.configure(amountused=temperature)
#             Hum.configure(amountused=Humidity)
#             Soil.configure(amountused=Soil_Temperature)
#             Mois.configure(amountused=soil_moisture)
#             Light.configure(amountused=light)
#             temperature=float(temperature)
#             soil_moisture=int(soil_moisture)
#             if temperature > 18 and temperature < 25 and soil_moisture > 50:
#                 print ("ok")
#                 plant_label.configure(text="GOOD CONDITION")
#             elif temperature < 18:
#                 Tap_label.configure(image=Tap_OFF)
#                 plant_label.configure(text="Maintain Temperature")
#                 Light_label.configure(image=Light_ON)
#             elif temperature > 25:
#                 plant_label.configure(text="Maintain Temperature")
#                 Fan_label.configure(image=Fan_ON)
#             elif soil_moisture > 50:
#                 print("Water Is Off")
#                 Tap_label.configure(image=Tap_OFF)
#                 plant_label.configure(text="Good Condition")
#             elif soil_moisture < 50:
#                 plant_label.configure(text="Water Is On")
#                 Tap_label.configure(image=Tap_ON)

#     Light.after(1000,read)

 

# splash screen
def splach_screen():

    image_frame=ttk.Frame(main_frame)
    image_frame.pack(fill=BOTH,expand=True)

    splash=TkinterVideo(image_frame)
    splash.load("splash.mp4")
    splash.pack(fill=BOTH,expand=True)
    splash.play()
    splash.after(3000,image_frame.destroy)



def home():
    global my_img1
    global my_img2
    global my_img3
    global my_img4
    global my_img5
    global my_img6
    global Fan_label
    global Light_label
    global Tap_label
    global soil_moisture
    global temperature
    global Humidity
    global light
    global Soil_Temperature 
    global Temp
    global Hum
    global Soil
    global Light
    global Mois
    global plant_label
    global Fan_OFF
    global Tap_ON
    global Light_OFF
    global Fan_ON
    global Tap_OFF
    global Light_ON

    # label frame

    Label_frame=ttk.LabelFrame(main_frame)
    Label_frame.grid(row=0,column=0)
    my_label=ttk.Label(Label_frame,text="GREEN HOUSE",font=("Helvetica",20),bootstyle="DANGER")
    my_label.grid(row=0,column=0)

    # fan_image

    Fan_ON=Image.open('fanon.png')
    Fan_ON=Fan_ON.resize((60,60),resample=Image.Resampling.LANCZOS)
    Fan_ON=ImageTk.PhotoImage(Fan_ON)

    Fan_OFF=Image.open('fanoff.png')
    Fan_OFF=Fan_OFF.resize((60,60),resample=Image.Resampling.LANCZOS)
    Fan_OFF=ImageTk.PhotoImage(Fan_OFF)
    Fan_label=ttk.Label(main_frame, image=Fan_OFF)
    Fan_label.grid(row=1,column=3)

    # light_image
    Light_ON=Image.open('lighton.png')
    Light_ON=Light_ON.resize((60,60),resample=Image.Resampling.LANCZOS)
    Light_ON=ImageTk.PhotoImage(Light_ON)

    Light_OFF=Image.open('lightsoff.png')
    Light_OFF=Light_OFF.resize((60,60),resample=Image.Resampling.LANCZOS)
    Light_OFF=ImageTk.PhotoImage(Light_OFF)
    Light_label=ttk.Label(main_frame, image=Light_OFF)
    Light_label.grid(row=1,column=3,rowspan=2)

    # tap_image

    Tap_ON=Image.open('tapon.png')
    Tap_ON=Tap_ON.resize((60,60),resample=Image.Resampling.LANCZOS)
    Tap_ON=ImageTk.PhotoImage(Tap_ON)

    Tap_OFF=Image.open('tapoff.png')
    Tap_OFF=Tap_OFF.resize((60,60),resample=Image.Resampling.LANCZOS)
    Tap_OFF=ImageTk.PhotoImage(Tap_OFF)
    Tap_label=ttk.Label(main_frame,image=Tap_OFF)
    Tap_label.grid(row=2,column=3)

    # meters

    Temp = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        
        metertype="full",
        subtext="Temperature",
        textright="c",
        textfont=['Times',26,'bold'],
        bootstyle='WARNING',
        interactive=True,
        stripethickness=8
    )
    Temp.grid(row=1, column=0, padx=10, pady=10)

    Hum = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        
        metertype="full",
        textright="%",
        textfont=['Times',26,'bold'],
        subtext="Humidity",
        bootstyle='DANGER',
        interactive=True,
        stripethickness=8
    )
    Hum.grid(row=1, column=1, padx=10, pady=10)

    Light = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        
        textfont=['Times',26,'bold'],
        metertype="full",
        textright="%",
        subtext="Light Intensity",
        bootstyle='PRIMARY',
        interactive=True,
        stripethickness=8
    )
    Light.grid(row=1, column=2, padx=10, pady=10,)

    Soil = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        
        metertype="full",
        textfont=['Times',26,'bold'],
        textright="%",
        subtext="Soil Temperature",
        bootstyle='INFO',
        interactive=True,
        stripethickness=8
    )
    Soil.grid(row=2, column=0, padx=10, pady=10)

    Mois = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        textfont=['Times',26,'bold'],
        metertype="full",
        subtext="Soil Moisture",
        textright="%",
        bootstyle='success',
        interactive=True,
        stripethickness=8
    )
    Mois.grid(row=2, column=1, padx=10, pady=10)

    # label

    plant_label=ttk.Label(main_frame)
    plant_label.grid(column=2,row=2,rowspan=2)

    plant_health_label = customtkinter.CTkLabel(master=plant_label,
                               text="PLANT HEALTH",
                               font=("Arial",20,"bold",UNDERLINE),
                               width=120,
                               height=25,
                               fg_color=("orange"),
                               corner_radius=8)
    plant_health_label.grid(row=0,column=0)

    plant_label = customtkinter.CTkLabel(master=plant_label,
                               text="GOOD",
                               font=("Arial",18,"bold"),
                               width=120,
                               height=25,
                               fg_color=("light green"),
                               corner_radius=8)
    plant_label.grid(row=1,column=0,pady=10)

    label3=ttk.Label(main_frame)
    label3.grid(row=3,column=1)

splach_screen()
root.after(3000,home)
# root.after(3000,read)
root.mainloop()