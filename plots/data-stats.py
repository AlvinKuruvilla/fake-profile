import matplotlib.pyplot as plt
import numpy as np

# Data
labels_gender = ['M', 'F', 'O']
sizes_gender = [38, 54, 8]

labels_handedness = ['Left', 'Right']
sizes_handedness = [13.6, 86.4]

labels_platform = ['Facebook', 'Instagram', 'Twitter']
sizes_platform = [29997, 22317, 18332]

labels_session = ['1', '2', '3', '4', '5', '6']
sizes_session = [2462, 1981, 1983, 1787, 1809, 1730]

# Adjusting the plot layout to keep one pie and one bar chart next to each other
fig, axs = plt.subplots(1, 4, figsize=(24, 6))

# Adjusting the color palette for better visibility and aesthetics
colors_adjusted = {
    'medium_blue': '#3a6ea5',
    'lighter_blue': '#6b9ed6',
    'peach': '#ed8a63',
    'tan': '#e9bf77',
    'gray': '#a8a8a8'
}

# Avg keystrokes per platform Bar Chart
axs[0].bar(labels_platform,
           sizes_platform,
           color=[colors_adjusted['lighter_blue'], colors_adjusted['medium_blue'], colors_adjusted['tan']])
axs[0].set_title('Avg keystrokes per platform')
axs[0].set_ylabel('Avg keystrokes')
axs[0].set_xlabel('platform')


# Gender Distribution Pie Chart with labels on the graph
axs[1].pie(sizes_gender,
           autopct='%1.1f%%',
           startangle=90,
           colors=[colors_adjusted['medium_blue'], colors_adjusted['tan'], colors_adjusted['gray']],
           wedgeprops=dict(width=0.1))
axs[1].set_title('Gender')
axs[1].legend(labels_gender, loc="best")


# Handedness Distribution Pie Chart with labels on the graph
axs[2].pie(sizes_handedness,
           autopct='%1.1f%%',
           startangle=90,
           colors=[colors_adjusted['medium_blue'], colors_adjusted['peach']],
           wedgeprops=dict(width=0.1))
axs[2].set_title('Handedness')
axs[2].legend(labels_handedness, loc="best")



# Avg keystrokes per session Bar Chart with adjusted width
bar_width = .75  # Making the bar thinner
axs[3].bar(labels_session,
           sizes_session,
           color=colors_adjusted['medium_blue'],
           width=bar_width)
axs[3].set_title('Avg keystrokes per video')
axs[3].set_ylabel('Avg keystrokes')
axs[3].set_xlabel('video #')

# Adjusting the layout for better presentation
plt.tight_layout()
plt.show()
