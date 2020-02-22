#analysis_script.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%

raw_data_df = pd.read_csv('data/raw_data.csv')

# %%

raw_data_df.head()

# %%

raw_data_array = np.array(raw_data_df)

# %%

cleaned_data_array = raw_data_array[1:, :]

# %%

d = 0.506
A0 = np.pi * (d / 2) ** 2
F = cleaned_data_array[:, 4]
stress = F / A0
strain = cleaned_data_array[:, 5] * 0.01

# %%

fig, ax = plt.subplots()
ax.plot(strain, stress)
# ax.set_xlabel("Strain (mm/mm)")
ax.set_ylabel("Stress (MPa)")
plt.show()

# %%

dir(ax)

# %%

ax.xaxis.label


# %%

def plot(strain, stress):
    fig, ax = plt.subplots()
    ax.plot(strain, stress)
    ax.set_xlabel("Strain (mm/mm)")
    ax.set_ylabel("Stress (MPa)")
    plt.show()

    return fig, ax


# %%

fig, ax = plot(strain, stress)

# %%

bool(fig)

# %%

dir(ax.xaxis.label)

# %%

ax.xaxis.label.get_text()

# %%

ax.xaxis.label

# %%