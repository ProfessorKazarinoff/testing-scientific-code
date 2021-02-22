#!/usr/bin/env python
# coding: utf-8

# In[1]:


# analysis.ipynb

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_data_df = pd.read_csv('data/raw_data.csv')

raw_data_array = np.array(raw_data_df)
cleaned_data_array = raw_data_array[1:,:]

d = 0.506
A0 = np.pi*(d/2)**2
F = cleaned_data_array[:,4]
stress = F/A0
strain = cleaned_data_array[:,5]*0.01
ts = np.max(stress)
te = np.max(strain)-np.min(strain)
print(f'Tensile Strength={ts}')
print(f'Total Extension={te}')

fig, ax = plt.subplots()
ax.plot(strain,stress)
ax.set_xlabel("Strain (mm/mm)")
ax.set_ylabel("Stress (MPa)")
plt.savefig("plot.png")
plt.show()

