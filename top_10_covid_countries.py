import pandas as pd

url = "https://covid19.who.int/WHO-COVID-19-global-table-data.csv"

data = pd.read_csv(url)
top_countries = data[1:11]

print(top_countries)
