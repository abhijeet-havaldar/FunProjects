import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

data = np.random.rand(10, 10)
sns.heatmap(data, cmap='coolwarm',annot=True, fmt='.2f')

plt.show()