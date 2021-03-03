import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("A001SB1_1.csv")
print(df)
#plt.scatter(df["year"], df["per capita income (US$)"], color='red', marker='x')
#plt.show()

#reg = linear_model.LinearRegression()
#reg.fit(df[["year"]], df["per capita income (US$)"])

# Predicting the GDP per capita of Canada in 2020
#p = reg.predict([[2020]])
#print(p)  # Predicted to be 41,288.69 US$

