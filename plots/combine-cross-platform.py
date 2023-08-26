import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data multiplied by 100
data = {
    "FI-T-ABS": [83.3333, 87.5, 87.5, 87.5, 87.5],
    "FI-T-SIM": [79.1667, 79.1667, 87.5, 87.5, 87.5],
    "FI-T-ITAD": [75, 79.1667, 79.1667, 83.3333, 83.3333],
    "FI-T-FMean": [87.5, 87.5, 87.5, 87.5, 87.5],
    "FI-T-FMedian": [83.3333, 87.5, 87.5, 87.5, 87.5],
    "FT-I-ABS": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "FT-I-SIM": [83.3333, 87.5, 91.6667, 91.6667, 91.6667],
    "FT-I-ITAD": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "FT-I-FMean": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "FT-I-FMedian": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "IF-T-ABS": [83.3333, 87.5, 87.5, 87.5, 87.5],
    "IF-T-SIM": [79.1667, 79.1667, 87.5, 87.5, 87.5],
    "IF-T-ITAD": [75, 79.1667, 79.1667, 83.3333, 83.3333],
    "IF-T-FMean": [87.5, 87.5, 87.5, 87.5, 87.5],
    "IF-T-FMedian": [83.3333, 87.5, 87.5, 87.5, 87.5],
    "IT-F-ABS": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "IT-F-SIM": [75, 83.3333, 83.3333, 87.5, 87.5],
    "IT-F-ITAD": [83.3333, 87.5, 91.6667, 95.8333, 95.8333],
    "IT-F-FMean": [87.5, 91.6667, 95.8333, 95.8333, 95.8333],
    "IT-F-FMedian": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "TF-I-ABS": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "TF-I-SIM": [83.3333, 87.5, 91.6667, 91.6667, 91.6667],
    "TF-I-ITAD": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "TF-I-FMean": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "TF-I-FMedian": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "TI-F-ABS": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
    "TI-F-SIM": [75, 83.3333, 83.3333, 87.5, 87.5],
    "TI-F-ITAD": [83.3333, 87.5, 91.6667, 95.8333, 95.8333],
    "TI-F-FMean": [87.5, 91.6667, 95.8333, 95.8333, 95.8333],
    "TI-F-FMedian": [91.6667, 91.6667, 91.6667, 91.6667, 91.6667],
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Sorting columns by median in ascending order
sorted_columns = df.median().sort_values().index

# Generate a custom color palette with the given blend
custom_palette = sns.blend_palette(["#7AB", "#EDA"], as_cmap=True)

# Generate a list of colors from the custom colormap
num_colors = df[sorted_columns].shape[1]  # number of columns
color_list = [custom_palette(i / (num_colors - 1)) for i in range(num_colors)]

# Plotting the sorted violin plot with the list of blended colors
plt.figure(figsize=(18, 10))
sns.violinplot(
    data=df[sorted_columns], inner="quartile", linewidth=0.5, palette=color_list
)
plt.xticks(rotation=90)
plt.ylabel("Rank accuracy (%)")
plt.xlabel("Verifier and platform")
plt.ylim(60, 110)
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)
# plt.title("Sorted Violin Plot with Custom Color Palette")
plt.grid(True)
plt.tight_layout()
plt.show()
