import serial

ser = serial.Serial('COM4', 9600, timeout=1)
global modified
global values

def read():
    global values
    global modified
    global soil_moisture
    global temperature
    global Humidity
    global Light
    global Soil_Temperature
    
    try:
        line = ser.readline().decode()   # read a byte
        sensor=line.split(",")
        modified = []
        values = []
        for line in sensor:
            modified.append(line.strip())
        print(modified)
        # if len(modified) == 5:
        #     values.append(modified)
        #     soil_moisture = values[0][0]
        #     temperature = values[0][1]
        #     Humidity = values[0][2]
        #     Light = values[0][3]
        #     Soil_Temperature = values[0][4]


           # Temp.configure(amountused=temperature)
           # Hum.configure(amountused=Humidity)
           # Soil.configure(amountused=Soil_Temperature)
           # Mois.configure(amountused=soil_moisture)
           # Light.configure(amountused=Light)
            
    except Exception as e:
        line = ser.readline().decode()   # read a byte
        sensor=line.split(",")
        modified = []
        values = []
        for line in sensor:
            modified.append(line.strip())
        print(modified)
        # if len(modified) == 5:
        #     values.append(modified)
        #     soil_moisture = values[0][0]
        #     temperature = values[0][1]
        #     Humidity = values[0][2]
            # Light = values[0][3]
            # Soil_Temperature = values[0][4]
            # Temp.configure(amountused=temperature)
            # Hum.configure(amountused=Humidity)
            # Soil.configure(amountused=Soil_Temperature)
            # Mois.configure(amountused=soil_moisture)
            # Light.configure(amountused=Light)


while True:
    read()