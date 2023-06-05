import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./dataset.csv")
ACT_composite_score = df['ACT composite score'].value_counts()
print("--------------------------------")
print("Distribution of ACT total score")
print("--------------------------------")
print('ACT total score')
ACT_composite_score.plot(kind='pie', title = 'ACT composite score', figsize =(6,6))
plt.show()
