import pandas as pd
import matplotlib.pyplot as plt

#a)
print("TASK A")
print("---------------------------")
data = pd.read_csv("data_C02_emission.csv")
categorical_cols = ["Make", "Model", "Vehicle Class", "Transmission", "Fuel Type"]

for col in categorical_cols:
    data[col] = data[col].astype("category")

plt.hist(data["CO2 Emissions (g/km)"], bins = 50)
plt.xlabel("CO2 Emissions (g/km)")
plt.ylabel("Frequency")
plt.title("CO2 Emissions (g/km)")
plt.show()

#b)
print("TASK B")
print("---------------------------")
data.plot.scatter( x = "Fuel Consumption City (L/100km)",
                   y = "CO2 Emissions (g/km)",
                   c = data["Fuel Type"].cat.codes,
                   cmap = "jet",)
print(data["Fuel Type"].cat)
plt.xlabel("Fuel Consumption City (L/100km)")
plt.ylabel("CO2 Emissions (g/km)")
plt.show()


#c)
print("TASK C")
print("---------------------------")
data.boxplot(column="Fuel Consumption Hwy (L/100km)", by = "Fuel Type" )
plt.xlabel("Fuel Consumption Hwy (L/100km)")
plt.show()

#d)
print("TASK D")
print("---------------------------")
cars_by_fuelType = data.groupby("Fuel Type").size()
cars_by_fuelType.plot(kind="bar")
plt.show()

#e)
print("TASK E")
print("---------------------------")
cylinders_by_CO2 = data.groupby("Cylinders",)["CO2 Emissions (g/km)"].mean()
cylinders_by_CO2.plot(kind="bar")
plt.ylabel("CO2 Emissions (g/km)")
plt.show()
