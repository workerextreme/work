import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./dataset.csv")

print("------------------------------------------------------------")
print("           COLLEGE GPA AND ACT COMPOSITE SCORE"              )
print("------------------------------------------------------------")
print(df['college gpa'].describe())

#Histogram
ax = df.plot.hist(column=['high school gpa'], by='SAT total score', figsize=(10, 8))
         
plt.show()

#Boxplot
plt.boxplot(df['high school gpa'])
plt.show()
