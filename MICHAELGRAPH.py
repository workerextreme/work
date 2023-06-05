import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./dataset.csv")

# Frequency Distribution
freq_dis = pd.crosstab(index=df['parental level of education'],columns="Frequency")
freq_dis["Relative Frequency"]=round(freq_dis['Frequency']/freq_dis['Frequency'].sum()*100,2)
freq_dis.loc["Total"]=freq_dis[['Frequency', 'Relative Frequency']].sum()
freq_dis.tail()

print("---------------------------------------------")
print("     DISTRIBUTION OF PARENTAL EDUCATION")
print("---------------------------------------------")
print(freq_dis)

State = df.groupby('parental level of education').size().reset_index(name = 'counts')

State.plot.bar(x='parental level of education',
               y='counts')
plt.show()
