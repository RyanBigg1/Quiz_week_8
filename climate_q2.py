import csv
import matplotlib.pyplot as plt

# Initialize empty lists to store data
years = []
co2_levels = []
temperature = []

# Open and read the CSV file
with open('climate.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        years.append(int(row['Year']))
        co2_levels.append(float(row['CO2']))
        temperature.append(float(row['Temperature']))

# create the figure and two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# C02 plot
ax1.plot(years, co2_levels, 'b--')
ax1.set_ylabel("CO2 Levels (ppm)")
ax1.set_title("Climate Data")
ax1.grid(True)

# Temperature plot
ax2.plot(years, temperature, 'r*-')
ax2.set_ylabel("Temperature (C)")
ax2.set_xlabel("Year")
ax2.grid(True)

plt.tight_layout()
plt.show()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

