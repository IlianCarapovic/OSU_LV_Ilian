from unicodedata import category

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data_C02_emission.csv")
#a)
print("TASK A")
print("---------------------------")
print(f"Number of measurements {len(data)}")
for col in data.columns:
    print(f"{col} : {data[col].dtype}")

print(f"Left out values{data.isnull().sum()}")
data_cleared = data.dropna()
print(f"Double values {data.duplicated().sum()}")
data_cleared = data.dropna()

categorical_cols = ["Make", "Model", "Vehicle Class", "Transmission", "Fuel Type"]

for col in categorical_cols:
    data_cleared[col] = data_cleared[col].astype("category")

print(data_cleared.info())
#b)
print("TASK B")
print("---------------------------")
most_consuming = data_cleared.nlargest(3, "Fuel Consumption City (L/100km)")
print("Most Consuming fuel")
print(most_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

least_consuming = data_cleared.nsmallest(3, "Fuel Consumption City (L/100km)")
print("Least Consuming fuel")
print(least_consuming[["Make", "Model", "Fuel Consumption City (L/100km)"]])

#c)
print("TASK C")
print("---------------------------")
motor_size_specified = data_cleared[(data_cleared["Engine Size (L)"] > 2.5) & (data_cleared["Engine Size (L)"] < 3.5)]
print(motor_size_specified[["Make", "Model", "Engine Size (L)"]].head(10))
print(motor_size_specified["CO2 Emissions (g/km)"].mean())

#d)
print("TASK D")
print("---------------------------")
audi_measurements = data_cleared[data_cleared["Make"] == "Audi"]
print(f"Number of measurements {len(audi_measurements)}") #audi_measurements.shape[0]
audi_measurements_filtered = audi_measurements[audi_measurements["Cylinders"] == 4]
print(f"CO2 consumption od audi with 4 cylinders {audi_measurements_filtered["CO2 Emissions (g/km)"].mean()}")

#e)
print("TASK E")
print("---------------------------")
cylinder_count = data_cleared["Cylinders"].value_counts().sort_index()
print(cylinder_count)

cylinder_emissions = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print(cylinder_emissions)

#f)
print("TASK F")
print("---------------------------")
diesel_cars = data_cleared[data_cleared["Fuel Type"] == "D"]
gasoline_cars = data_cleared[(data_cleared["Fuel Type"] == "X")]
print(f"Gasoline cars {gasoline_cars.shape[0]}, gasoline consumption = {gasoline_cars["Fuel Consumption City (L/100km)"].mean()}, Medijan = {gasoline_cars["Fuel Consumption City (L/100km)"].median()}")
print(f"Diesel cars {diesel_cars.shape[0]}, diesel consumption = {diesel_cars["Fuel Consumption City (L/100km)"].mean()}, Medijan = {diesel_cars["Fuel Consumption City (L/100km)"].median()}")

#g)
print("TASK F")
print("---------------------------")
cars = data_cleared[(data_cleared["Fuel Type"] == "D") & (data_cleared["Cylinders"] ==4)]
wanted_car = cars.nlargest(1, "Fuel Consumption City (L/100km)")
print(wanted_car[["Make","Model","Fuel Consumption City (L/100km)"]])

#h)
print("TASK H")
print("---------------------------")
manual_cars = data_cleared[data_cleared["Transmission"].str.startswith("M")]
print(f"Manual transmission cars = {manual_cars.shape[0]}")

#i
print("TASK I")
print("---------------------------")
numerical_data = data_cleared.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_data.corr()

print(correlation_matrix.describe())