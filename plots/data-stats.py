import matplotlib.pyplot as plt
import numpy as np

def remove_spines(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Data definitions
labels_gender = ['M', 'F', 'Others']
sizes_gender = [38, 54, 8]

labels_handedness = ['Left', 'Right']
sizes_handedness = [13.6, 86.4]

labels_platform = ['Facebook', 'Instagram', 'Twitter']
sizes_platform = [29997, 22317, 18332]

labels_session = ['1', '2', '3', '4', '5', '6']
sizes_session = [2462, 1981, 1983, 1787, 1809, 1730]

# Adjusting the color palette for better visibility and aesthetics
colors_adjusted = {
    'medium_blue': '#3a6ea5',
    'lighter_blue': '#6b9ed6',
    'peach': '#ed8a63',
    'tan': '#e9bf77',
    'gray': '#a8a8a8'
}

# Generate reversed shades for the last bar graph
colors_last_graph_reversed = plt.cm.Blues(np.linspace(0.4, 1, len(sizes_session)))[np.argsort(-np.array(sizes_session))]

# Create main figure
fig = plt.figure(figsize=(24, 6))

# Define grid layout
gs = fig.add_gridspec(1, 4)

# Subfigure for the first bar chart

ax1 = fig.add_subplot(gs[0, 0])
bars1 = ax1.bar(labels_platform,
                sizes_platform,
                color=[colors_adjusted['lighter_blue'], colors_adjusted['medium_blue'], colors_adjusted['tan']],
                edgecolor='none')
# ax1.set_title('keystrokes per platform')
ax1.set_ylabel('# of keystrokes')
ax1.set_xlabel('Platform')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Add numbers on top of bars for the first bar chart
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', rotation=90)

# Subfigure for the second bar chart
ax2 = fig.add_subplot(gs[0, 1])
bars2 = ax2.bar(labels_session,
                sizes_session,
                color=colors_last_graph_reversed[np.argsort(np.argsort(sizes_session))],
                width=0.75,
                edgecolor='none')
# ax2.set_title('keystrokes per video')

ax2.set_xlabel('video #')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Add numbers on top of bars for the second bar chart and remove y-axis label
for bar in bars2:
    height = bar.get_height()
    ax2.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', rotation=90)
ax2.set_ylabel('# of keystrokes')


remove_spines(ax1)
remove_spines(ax2)
ax1.set_yticks([])
ax2.set_yticks([])


# Subfigure for the first pie chart (Gender)
ax3 = fig.add_subplot(gs[0, 2])
gender_pie = ax3.pie(sizes_gender,
                     autopct='%1.1f%%',
                     startangle=90,
                     colors=[colors_adjusted['medium_blue'], colors_adjusted['tan'], colors_adjusted['gray']],
                     wedgeprops=dict(width=0.1))
ax3.set_title('Gender')
ax3.legend(labels_gender, loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=len(labels_gender))

# Subfigure for the second pie chart (Handedness)
ax4 = fig.add_subplot(gs[0, 3])
handedness_pie = ax4.pie(sizes_handedness,
                         autopct='%1.1f%%',
                         startangle=90,
                         colors=[colors_adjusted['medium_blue'], colors_adjusted['peach']],
                         wedgeprops=dict(width=0.1))
ax4.set_title('Handedness')
ax4.legend(labels_handedness, loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=len(labels_handedness))

# Adjusting the layout for better presentation
plt.tight_layout()
plt.show()
