""" 
Created on : 31/05/23 3:05 pm
@author : ds  
"""

from hulearn.datasets import load_titanic
from sklego.datasets import load_penguins
from hulearn.experimental.interactive import InteractiveCharts

df = load_titanic(as_frame=True)
print(df.head())


df = load_penguins(as_frame=True).dropna()
clf = InteractiveCharts(df, labels="species")

clf.add_chart(x="bill_length_mm", y="bill_depth_mm")

