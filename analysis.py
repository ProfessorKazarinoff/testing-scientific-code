# analysis.py

import sys
import platform

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp


def get_info():
    print(f"Python version: {platform.python_version()}")
    # sys.version_info or sys.version_info.major and sys.version_info.minor
    print(f"NumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Matplotlib version: {mp.__version__}")
    print()
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"encoding: {sys.getfilesystemencoding()}")
    return {
        "Python_major_version": sys.version_info.major,
        "Python_minor_version": sys.version_info.minor,
    }


def import_data(f_name):
    df = pd.read_csv(f_name)
    np_raw_array = np.array(df)
    np_array = np_raw_array[1:, :]
    return np_array


def get_stress_and_strain(cleaned_data_array):
    d = 0.506
    A0 = np.pi * (d / 2) ** 2
    F = cleaned_data_array[:, 4]
    stress = F / A0
    strain = cleaned_data_array[:, 5] * 0.01
    return stress, strain


def plot(x, y, title, x_label, y_label):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()
    return fig, ax


def get_tensile_strength(stress, strain):
    return np.max(stress).round(3)


def get_total_extension(stress, strain):
    return np.max(strain) - np.min(strain)


def main():
    fname = "data/raw_data.csv"

    get_info()
    data_array = import_data(fname)
    stress, strain = get_stress_and_strain(data_array)
    plot(strain, stress, "Stress Strain Curve", "Strain (mm/mm)", "Stress (MPa)")
    ts = get_tensile_strength(stress, strain)
    te = get_total_extension(stress, strain)
    print(f"Tensile Strength: {ts}, Total Extension: {te}")


if __name__ == "__main__":
    main()
