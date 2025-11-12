import pandas as pd

player = {
    "Last Name": ["Bacot", "Davis", "Cadeau", "High", "Trimble",
                  "Withers", "Washington", "Okonkwo", "James", "Powell"],
    "First Name": ["Armando", "RJ", "Elliot", "Zayden", "Seth",
                   "Jae'Lyn", "Jalen", "Duwe", "Creighton", "Rob"],
    "Height": [83, 72, 73, 81, 75, 80, 82, 78, 78, 77],
    "Weight": [240, 180, 180, 225, 195, 215, 230, 235, 190, 200]
}

data = pd.DataFrame(player)

# bmi = weight in kg/ height in meters squared
data["BMI"] = (data["Weight"] / 2.205) / ((data["Height"] / 39.37) ** 2)

# Round to two decimal places
data["BMI"] = data["BMI"].round(2)

print(data)

data.to_csv("bmi.csv", index=False)
