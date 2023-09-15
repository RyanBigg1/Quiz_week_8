import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

years = []
co2 = []
temp = []

# Execute an SQL query to fetch data from a specific table in the database
cursor.execute('SELECT Year, CO2, Temperature FROM ClimateData')

# Fetch all the rows into a list
data = cursor.fetchall()

# Separate data into years, co2, and temp lists
years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

# Close the database connection
conn.close()

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
plt.savefig("co2_temp_1.png") 
