import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.scatterplot(data=mydata,x='example1',y='example2')
sns.barplot(data=mydata,x='example1',y='example2')  
sns.lineplot(data=mydata,x='example1',y='example2') 
sns.histplot(data=mydata,x='example1')
sns.kdeplot(data=mydata,x='example1',fill=True,ci=None,fill=None) 
sns.boxplot(data=mydata,x='example1')
sns.boxplot(data=mydata,x='example1',y='example1')

sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", kind="kde")
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
sns.displot(tips, x="size", discrete=True)
sns.displot(penguins, x="flipper_length_mm", hue="sex", multiple="dodge")
