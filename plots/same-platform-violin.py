# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def remove_spines(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)


# Define the data
data_violin = {
    "F-ABS": [0.625, 0.708333, 0.791667, 0.833333, 0.875],
    "F-SIM": [0.708333, 0.791667, 0.875, 0.916667, 0.958333],
    "F-ITAD": [0.666667, 0.833333, 0.833333, 0.875, 0.875],
    "F-FMean": [0.916667, 1, 1, 1, 1],
    "F-FMedian": [0.666667, 0.791667, 0.875, 0.916667, 0.958333],
    "I-ABS": [0.458333, 0.5, 0.708333, 0.75, 0.791667],
    "I-SIM": [0.708333, 0.791667, 0.791667, 0.833333, 0.833333],
    "I-ITAD": [0.75, 0.833333, 0.833333, 0.875, 0.875],
    "I-FMean": [0.791667, 0.833333, 0.875, 0.875, 0.875],
    "I-FMedian": [0.5, 0.583333, 0.708333, 0.791667, 0.833333],
    "T-ABS": [0.5, 0.75, 0.791667, 0.833333, 0.833333],
    "T-SIM": [0.583333, 0.666667, 0.75, 0.791667, 0.833333],
    "T-ITAD": [0.5, 0.708333, 0.833333, 0.875, 0.875],
    "T-FMean": [0.75, 0.791667, 0.875, 0.875, 0.875],
    "T-FMedian": [0.625, 0.708333, 0.791667, 0.833333, 0.833333],
}

# Convert the data to DataFrame
df_violin = pd.DataFrame(data_violin)

# Multiply every value by 100
df_violin_100 = df_violin * 100

# Calculate the median for ordering
medians = df_violin_100.median().sort_values()

# Order data by medians
df_violin_ordered = df_violin_100[medians.index]

# Create the figure and define its size
plt.figure(figsize=(18, 8))

# Use a more scientific color palette
palette = sns.color_palette("blend:#7AB,#EDA", len(df_violin_ordered.columns))

# Generate ordered violin plots
sns.violinplot(data=df_violin_ordered, palette=palette, inner=None, linewidth=0)

# Overlay with swarm plots to display individual data points
sns.swarmplot(
    data=df_violin_ordered, color="black", edgecolor="gray", linewidth=0.5, size=4
)

# Set plot labels, titles, and other properties
plt.xticks(rotation=90)
# plt.title('Algorithm Performance Distribution on Social Media Platforms (Ordered by Median Performance)')
plt.ylabel("Rank accuracy (%)")
plt.xlabel("Verifier and platform")
# Remove the border/spines
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)
plt.ylim(40, 110)
plt.tight_layout()
plt.grid(True)
# Display the plot
plt.show()
