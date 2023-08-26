import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data
data = {
    "F-I-ABS": [0.75, 0.75, 0.833333, 0.916667, 0.916667],
    "F-I-SIM": [0.791667, 0.791667, 0.791667, 0.833333, 0.875],
    "F-I-ITAD": [0.708333, 0.791667, 0.791667, 0.791667, 0.833333],
    "F-I-FMean": [0.791667, 0.916667, 0.916667, 0.916667, 0.916667],
    "F-I-FMedian": [0.75, 0.75, 0.833333, 0.916667, 0.916667],
    "F-T-ABS": [0.791667, 0.833333, 0.875, 0.875, 0.875],
    "F-T-SIM": [0.708333, 0.791667, 0.833333, 0.833333, 0.833333],
    "F-T-ITAD": [0.708333, 0.791667, 0.791667, 0.791667, 0.833333],
    "F-T-FMean": [0.833333, 0.875, 0.875, 0.875, 0.875],
    "F-T-FMedian": [0.791667, 0.833333, 0.875, 0.875, 0.875],
    "I-F-ABS": [0.791667, 0.833333, 0.875, 0.916667, 0.916667],
    "I-F-SIM": [0.75, 0.833333, 0.833333, 0.875, 0.875],
    "I-F-ITAD": [0.75, 0.791667, 0.875, 0.916667, 0.916667],
    "I-F-FMean": [0.875, 0.916667, 0.916667, 0.916667, 0.916667],
    "I-F-FMedian": [0.791667, 0.833333, 0.875, 0.916667, 0.916667],
    "I-T-ABS": [0.833333, 0.833333, 0.833333, 0.833333, 0.833333],
    "I-T-SIM": [0.666667, 0.708333, 0.791667, 0.833333, 0.833333],
    "I-T-ITAD": [0.625, 0.75, 0.791667, 0.791667, 0.833333],
    "I-T-FMean": [0.833333, 0.833333, 0.833333, 0.833333, 0.833333],
    "I-T-FMedian": [0.833333, 0.833333, 0.833333, 0.833333, 0.833333],
    "T-F-ABS": [0.791667, 0.791667, 0.791667, 0.791667, 0.833333],
    "T-F-SIM": [0.708333, 0.75, 0.791667, 0.833333, 0.875],
    "T-F-ITAD": [0.666667, 0.75, 0.833333, 0.833333, 0.833333],
    "T-F-FMean": [0.833333, 0.833333, 0.875, 0.875, 0.875],
    "T-F-FMedian": [0.791667, 0.791667, 0.791667, 0.791667, 0.833333],
    "T-I-ABS": [0.75, 0.833333, 0.833333, 0.833333, 0.833333],
    "T-I-SIM": [0.75, 0.833333, 0.833333, 0.833333, 0.833333],
    "T-I-ITAD": [0.75, 0.75, 0.791667, 0.791667, 0.791667],
    "T-I-FMean": [0.833333, 0.833333, 0.833333, 0.833333, 0.833333],
    "T-I-FMedian": [0.75, 0.833333, 0.833333, 0.833333, 0.833333],
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)
# Multiply each value by 100
df = df * 100
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
# plt.title("Sorted Violin Plot with Custom Color Palette")
plt.ylabel("Rank accuracy (%)")
plt.xlabel("Verifier and platform")
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)
plt.tight_layout()
plt.grid(True)
plt.show()
