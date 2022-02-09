import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart.csv")
df2 = pd.read_csv("data.csv")
fig = px.scatter(df, x = "Year", y = "Per capita income", color = "Country", title = "Per capita income")
#fig = px.scatter(df2, x = "Country", y = "InternetUsers", size = "Percentage", color = "Country")

fig.show()