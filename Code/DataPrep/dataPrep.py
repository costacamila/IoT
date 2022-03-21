import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = '../../Data/Processed/inside.csv'
data = pd.read_csv(url)
data.columns = ["id", "room_id", "noted_date", "temp", "out/in"]

data['simple_id'] = data.index + 1
data["noted_date"] = pd.to_datetime(data["noted_date"])
new_data = data.drop(['id'], axis=1)
new_data = new_data.reindex(columns=["simple_id", "room_id", "noted_date", "temp", "out/in"])
