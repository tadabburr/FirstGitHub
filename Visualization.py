# Below is an example program for data visualization
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style= "ticks", color_codes=True )
nayya = sns.load_dataset("titanic") # dataset load in variable nayya
#print (nayya)                      print the tatanic view
sns.catplot(x="sex",y='age', hue='survived', kind='bar', data= nayya) # Graph Design
plt.show()                          # graph print
