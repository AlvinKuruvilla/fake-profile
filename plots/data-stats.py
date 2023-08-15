# Plot adjustments
fig, axs = plt.subplots(1, 4, figsize=(20, 5))

# Gender pie chart
axs[0].pie(sizes_gender, labels=labels_gender, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b2ff','#99ff99'])
axs[0].set_title('Gender Distribution')

# Handedness pie chart
axs[1].pie(sizes_handedness, labels=labels_handedness, autopct='%1.1f%%', startangle=90, colors=['#ffcc99', '#c2c2f0'])
axs[1].set_title('Handedness Distribution')

# Platform bar chart
axs[2].bar(labels_platform, sizes_platform, color=['#ff9999','#66b2ff','#99ff99'])
axs[2].set_title('Average Keystrokes per Platform')
axs[2].set_ylabel('Average Keystrokes')
axs[2].set_xlabel('Platform')

# Session bar chart
axs[3].bar(labels_session, sizes_session, color='#c2c2f0')
axs[3].set_title('Average Keystrokes per Session')
axs[3].set_ylabel('Average Keystrokes')
axs[3].set_xlabel('Session Number')

# Adjust layout
plt.tight_layout()
plt.show()
