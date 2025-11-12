import pandas as pd

roster = ["Bacot", "Davis", "Cadeau"]
player = {"Last Name": roster,
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [83, 72, 731],
          "weight": [240,180,1801]}
data = pd.DataFrame(player)
print(data)