import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [83, 72, 731],
          "weight": [240,180, 180]
          }
data = pd.DataFrame(player)
print(data)