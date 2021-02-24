# analysis.py

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def import_data(f_path):
    df = pd.read_csv(f_path)
    np_raw_array = np.array(df)
    return np_raw_array


def clean_data(raw_np_array):
    np_array = raw_np_array[1:, :]
    return np_array


def get_stress_and_strain(cleaned_data_array):
    d = 0.506
    A0 = np.pi * (d / 2) ** 2
    F = cleaned_data_array[:, 4] * 0.001
    stress = F / A0
    strain = cleaned_data_array[:, 5] * 0.01
    return stress, strain


def plot(x, y, title, x_label, y_label, f_name):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    save_plot(fig, f_name)
    plt.show()
    return fig, ax


def save_plot(fig, fname):
    fig.savefig(fname)
    return fig


def get_tensile_strength(stress, strain):
    return np.max(stress).round(3)


def get_total_extension(stress, strain):
    return np.max(strain) - np.min(strain)


def main():
    raw_data_path = Path(Path.cwd(), "data", "raw_data.csv")
    raw_data_array = import_data(raw_data_path)
    clean_data_array = clean_data(raw_data_array)
    stress, strain = get_stress_and_strain(clean_data_array)
    title = "Stress Strain Curve"
    xlabel = "Strain (mm/mm)"
    ylabel = "Stress (MPa)"
    f_name = "plot.png"
    plot(strain, stress, title, xlabel, ylabel, f_name)
    ts = get_tensile_strength(stress, strain)
    te = get_total_extension(stress, strain)
    print(f"Tensile Strength: {ts}, Total Extension: {te}")


if __name__ == "__main__":
    main()
