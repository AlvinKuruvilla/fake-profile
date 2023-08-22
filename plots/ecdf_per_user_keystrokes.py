import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
# Data
user_ids = [i for i in range(1, 27) if i != 22]  # Excluding 22 as it's missing from the data
sample_counts = [1193, 755, 814, 745, 426, 867, 376, 1138, 587, 1132,
                 1122, 1128, 1871, 1194, 931, 742, 984, 703, 2537,
                 768, 1043, 930, 699, 512, 362]

# Calculate ECDF
x = np.sort(sample_counts)
y = np.arange(1, len(x) + 1) / len(x)

# Defining the color palette
colors_adjusted = {
    'silver': '#e6e6fa',
    'gray': '#808080'
}

from scipy.interpolate import make_interp_spline
# Interpolating the data for a smoother curve
x_new = np.linspace(min(x), max(x), 500)  # Create 500 evenly spaced values within the range of x
y_new = np.interp(x_new, x, y)  # Interpolate a smooth curve based on original x and y

# Using a spline interpolation to further smooth the ECDF
x_spline = np.linspace(x_new.min(), x_new.max(), 1000)
spline = make_interp_spline(x_new, y_new, k=3)  # Using a 3rd degree spline
y_spline = spline(x_spline)

# Plotting the further smoothed ECDF
plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")
plt.plot(x_spline, y_spline, linestyle='-', color=colors_adjusted['gray'])
plt.fill_between(x_spline, y_spline, color=colors_adjusted['silver'], alpha=0.2)
# plt.title('ECDF', fontsize=16)
plt.xlabel('number of keystrokes', fontsize=14)
plt.ylabel('F(x)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which="both", ls="--", c='0.7')
 # Polishing the plot
sns.despine(left=True, bottom=True)

plt.show()
